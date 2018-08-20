import io
import json
import os
from collections import *

idSnippetsFileName = "SnippetsId.tsv"
featuresFileName = "featuresPSI.tsv"
statisticNumbersFileName = "statisticsPSI.txt"


class Counter(object):
    def __init__(self, lines, files, snippets):
        self.lines = lines
        self.files = files
        self.snippets = snippets

    def incLine(self):
        self.lines = self.lines + 1

    def incFile(self):
        self.files = self.files + 1

    def incSnippets(self):
        self.snippets = self.snippets + 1

    def getLines(self):
        return self.lines

    def getFiles(self):
        return self.files

    def getSnippets(self):
        return self.snippets

def bfs(a):
    for node in a:
        if 'children' in node:
            print(node)
            bfs(node['children'])

def childrenNumber(a):
    result = 0
    for node in a:
        if 'children' in node:
            result += childrenNumber(node['children'])
        else:
            result += 1
    return result

def nodeNumber(a):
    result = 0
    for node in a:
        result += 1
        if 'children' in node:
            result += nodeNumber(node['children'])
    return result

def successorNumber(node):
    result = 0
    if 'children' in node:
        result = len(node['children'])
    return result

def treeMap(tree, func):
    result = 0
    for node in tree:
        if func(node):
            result += 1
        if 'children' in node:
            result += treeMap(node['children'], func)
    return result

def treeReduce(tree, func):
    result = 0
    def treeReduceRecursive(tree, func, depth):
        result = 0
        for node in tree:
            if func(node, depth):
                result += 1
            if 'children' in node:
                result += treeReduceRecursive(node['children'], func, depth + 1)
        return result
    return treeReduceRecursive(tree, func, 0)

def countNodeTypes(a):
    cnt = Counter()
    for node in a:
        cnt[node['type']] += 1
        if 'children' in node:
            cnt += countNodeTypes(node['children'])
    return cnt


def feature_extractor_PSI():
    try:
        # c = Counter(0, 0, 0)
        statisticNumbersFile = open(statisticNumbersFileName, 'w')
        idSnippetsFile = open(idSnippetsFileName, 'r')
        featuresFile = open(featuresFileName, 'w')
        for line in idSnippetsFile:
            arr = line.split('\t')
            id = int(arr[0])
            path = arr[1].replace('\Snippets', '\PSI\PSI')
            path = path.rstrip()
            if os.path.exists(path):
                psiFile = open(path, 'r')
                # c.incFile()
                
                nodes = psiFile.read()
                a = json.loads(nodes)

                featureChildrenNumber = childrenNumber(a))
                numberOfNodes = nodeNumber(a)
                featureNumberOfNodes = numberOfNodes

                featureSuccessorNumberOne = treeMap(a, lambda node: successorNumber(node) == 1)
                featureSuccessorNumberTwo = treeMap(a, lambda node: successorNumber(node) == 2)
                featureSuccessorNumberMoreThanTwo = treeMap(a, lambda node: successorNumber(node) > 2)

                featureDepthOne = treeReduce(a, lambda _, depth: depth == 1)
                featureDepthTwo = treeReduce(a, lambda _, depth: depth == 2)
                featureDepthMoreThanTwo = treeReduce(a, lambda _, depth: depth > 2)

                featureSuccessorNumberOneDepthOne = treeReduce(a, lambda node, depth: successorNumber(node) == 1 and depth == 1)
                featureSuccessorNumberOneDepthTwo = treeReduce(a, lambda node, depth: successorNumber(node) == 1 and depth == 2)
                featureSuccessorNumberTwoDepthOne = treeReduce(a, lambda node, depth: successorNumber(node) == 2 and depth == 1)
                featureSuccessorNumberTwoDepthTwo = treeReduce(a, lambda node, depth: successorNumber(node) == 2 and depth == 2)
                featureSuccessorNumberMoreThanTwoDepthMoreThanTwo = treeReduce(a, lambda node, depth: successorNumber(node) > 2 and depth > 2)

                featureNumberOfNodesLess15 = numberOfNodes < 15
                featureNumberOfNodesMore15 = numberOfNodes >= 15 and numberOfNodes <= 500
                featureNumberOfNodesMore500 = numberOfNodes > 500

                featureCountNodeTypes = countNodeTypes(a)

                featureMaxDepthPSI = 0.0
                featureNumberOfNodes = 0.0
                featureNumberOfSpaces = 0.0
                featureMaxNumberOfChildren = 0.0
                featureMaxNumberOfSpacesWithRatio = 0.0
                featureAVGNumberOfSpacesWithRatio = 0.0

                featureNumberOfPSIElements = 0.0
                featureNumberOfPsiWhiteSpace = 0.0
                featureAVGNumberOfPSIElements = 0.0
                featureAVGNumberOfPsiWhiteSpace = 0.0
                featureNumberOfLines = 0.0
                featureAVGLengthOfLines = 0.0

                featureNumberOfIdentifiers = 0.0
                featureNumberOfFuns = 0.0
                featureNumberOfLPAR = 0.0
                featureNumberOfRPAR = 0.0
                featureNumberOfCOLON = 0.0
                featureNumberOfQUEST = 0.0
                featureNumberOfLBRACE = 0.0
                featureNumberOfRBRACE = 0.0
                featureNumberOfSAFE_ACCESS = 0.0
                featureNumberOfEQ = 0.0
                featureNumberOfOPEN_QUOTE = 0.0
                featureNumberOfREGULAR_STRING_PART = 0.0
                featureNumberOfCLOSING_QUOTE = 0.0
                featureNumberOfAS_SAFE = 0.0
                featureNumberOfELVIS = 0.0
                featureNumberOfTrue = 0.0
                featureNumberOfFalse = 0.0

                listOfLengthLines = []

                listOfNumberOfSpacesWithRatio = []
                # featureAVGNumberOfChildren = 0.0

                numNodes = 0
                numChildren = 0
                numLines = 0
                maxDepthElement = 0
                maxChildrenNumber = 0
                for psiLine in psiFile:
                    offset = 0
                    numSpaces = 0
                    numLines += 1
                    f = True
                    for c in psiLine:
                        if c == ' ':
                            numSpaces += 1
                            if f:
                                offset += 1
                        elif c == '{':
                            numNodes += 1
                            numChildren += 1
                            f = False
                        elif c == '}':
                            maxChildrenNumber = max(maxChildrenNumber, numChildren)
                            numChildren -= 1
                            f = False
                        else:
                            f = False
                    if "PsiElement" in psiLine:
                        featureNumberOfPSIElements += 1.0
                    if "PsiWhiteSpace" in psiLine:
                        featureNumberOfPsiWhiteSpace += 1.0
                    if "IDENTIFIER" in psiLine:
                        featureNumberOfIdentifiers += 1.0
                    if "fun" in psiLine:
                        featureNumberOfFuns += 1.0
                    if "LPAR" in psiLine:
                        featureNumberOfLPAR += 1.0
                    if "RPAR" in psiLine:
                        featureNumberOfRPAR += 1.0
                    if "COLON" in psiLine:
                        featureNumberOfCOLON += 1.0
                    if "QUEST" in psiLine:
                        featureNumberOfQUEST += 1.0
                    if "LBRACE" in psiLine:
                        featureNumberOfLBRACE += 1.0
                    if "RBRACE" in psiLine:
                        featureNumberOfRBRACE += 1.0
                    if "SAFE_ACCESS" in psiLine:
                        featureNumberOfSAFE_ACCESS += 1.0
                    if "EQ" in psiLine:
                        featureNumberOfEQ += 1.0
                    if "OPEN_QUOTE" in psiLine:
                        featureNumberOfOPEN_QUOTE += 1.0
                    if "REGULAR_STRING_PART" in psiLine:
                        featureNumberOfREGULAR_STRING_PART += 1.0
                    if "CLOSING_QUOTE" in psiLine:
                        featureNumberOfCLOSING_QUOTE += 1.0
                    if "AS_SAFE" in psiLine:
                        featureNumberOfAS_SAFE += 1.0
                    if "ELVIS" in psiLine:
                        featureNumberOfELVIS += 1.0
                    if "true" in psiLine:
                        featureNumberOfTrue += 1.0
                    if "false" in psiLine:
                        featureNumberOfFalse += 1.0
                    depth = offset // 2
                    maxDepthElement = max(maxDepthElement, depth)
                    numSpacesWithRatio = numSpaces / len(psiLine)
                    listOfNumberOfSpacesWithRatio.append(numSpacesWithRatio)
                    listOfLengthLines.append(len(psiLine))
                    featureMaxNumberOfSpacesWithRatio = max(featureMaxNumberOfSpacesWithRatio, numSpacesWithRatio)
                featureMaxDepthPSI = float(maxDepthElement)
                featureNumberOfNodes = float(numNodes)
                featureNumberOfSpaces = float(numSpaces)
                featureMaxNumberOfChildren = float(maxChildrenNumber)
                featureAVGNumberOfSpacesWithRatio = \
                    sum(listOfNumberOfSpacesWithRatio) / len(listOfNumberOfSpacesWithRatio)
                featureAVGLengthOfLines = \
                    sum(listOfLengthLines) / numLines
                featureAVGNumberOfPSIElements = featureNumberOfPSIElements / numLines
                featureAVGNumberOfPsiWhiteSpace = featureNumberOfPsiWhiteSpace / numLines
                featureNumberOfLines = float(numLines)
                featuresList = [featureMaxDepthPSI, featureMaxNumberOfChildren, featureNumberOfNodes,
                                featureNumberOfSpaces, featureMaxNumberOfSpacesWithRatio,
                                featureAVGNumberOfSpacesWithRatio,
                                featureNumberOfPSIElements, featureNumberOfPsiWhiteSpace,
                                featureAVGNumberOfPSIElements, featureAVGNumberOfPsiWhiteSpace,
                                featureNumberOfLines, featureAVGLengthOfLines, featureNumberOfIdentifiers,
                                featureNumberOfLPAR, featureNumberOfRPAR, featureNumberOfCOLON, featureNumberOfQUEST,
                                featureNumberOfLBRACE, featureNumberOfRBRACE, featureNumberOfSAFE_ACCESS,
                                featureNumberOfEQ, featureNumberOfOPEN_QUOTE, featureNumberOfREGULAR_STRING_PART,
                                featureNumberOfCLOSING_QUOTE, featureNumberOfAS_SAFE, featureNumberOfELVIS,
                                featureNumberOfTrue, featureNumberOfFalse,
                                featureChildrenNumber, featureNumberOfNodes, featureSuccessorNumberOne,
                                featureSuccessorNumberTwo,featureSuccessorNumberMoreThanTwo,featureDepthOne,
                                featureDepthTwo, featureDepthMoreThanTwo, featureSuccessorNumberOneDepthOne,
                                featureSuccessorNumberOneDepthTwo, featureSuccessorNumberTwoDepthOne,
                                featureSuccessorNumberTwoDepthTwo,
                                featureSuccessorNumberMoreThanTwoDepthMoreThanTwo,
                                featureNumberOfNodesLess15, featureNumberOfNodesMore15,
                                featureNumberOfNodesMore500, featureCountNodeTypes]
                featuresFile.write(str(id))
                for feature in featuresList:
                    featuresFile.write("\t" + str(feature))
                featuresFile.write("\n")

        statisticNumbersFile.write("PSI Files = " + str(c.getFiles()))
        statisticNumbersFile.write("\n")
        # statisticNumbersFile.write("Lines = " + str(c.getLines()))
        # statisticNumbersFile.write("\n")
        # statisticNumbersFile.write("Snippets = " + str(c.getSnippets()))
        # statisticNumbersFile.write("\n")

        featuresFile.close()
        idSnippetsFile.close()
        statisticNumbersFile.close()
    except:
        pass


feature_extractor_PSI()
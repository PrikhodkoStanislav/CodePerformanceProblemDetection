import os

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

                featureMaxDepthPSI = 0.0
                featureNumberOfNodes = 0.0
                featureNumberOfSpaces = 0.0
                featureMaxNumberOfChildren = 0.0
                featureMaxNumberOfSpacesWithRatio = 0.0
                featureAVGNumberOfSpacesWithRatio = 0.0

                listOfNumberOfSpacesWithRatio = []
                # featureAVGNumberOfChildren = 0.0

                numNodes = 0
                numChildren = 0
                maxDepthElement = 0
                maxChildrenNumber = 0
                for psiLine in psiFile:
                    offset = 0
                    numSpaces = 0
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
                    depth = offset // 2
                    maxDepthElement = max(maxDepthElement, depth)
                    numSpacesWithRatio = numSpaces / len(psiLine)
                    listOfNumberOfSpacesWithRatio.append(numSpacesWithRatio)
                    featureMaxNumberOfSpacesWithRatio = max(featureMaxNumberOfSpacesWithRatio, numSpacesWithRatio)
                featureMaxDepthPSI = float(maxDepthElement)
                featureNumberOfNodes = float(numNodes)
                featureNumberOfSpaces = float(numSpaces)
                featureMaxNumberOfChildren = float(maxChildrenNumber)
                featureAVGNumberOfSpacesWithRatio =\
                    sum(listOfNumberOfSpacesWithRatio) / len(listOfNumberOfSpacesWithRatio)
                featuresList = [ featureMaxDepthPSI, featureMaxNumberOfChildren, featureNumberOfNodes,
                                 featureNumberOfSpaces, featureMaxNumberOfSpacesWithRatio,
                                 featureAVGNumberOfSpacesWithRatio]
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

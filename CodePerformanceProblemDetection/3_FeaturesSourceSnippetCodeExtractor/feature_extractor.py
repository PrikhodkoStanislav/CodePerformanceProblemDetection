import math
import os

folder = "FilesSourcesFromGithub_Snippets_2"
#folder = "Snippets"

idSnippetsFileName = "SnippetsId.tsv"
featuresFileName = "features.tsv"
statisticNumbersFileName = "statistics.txt"

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

def feature_extractor_sourcecode_snippets():
    try:
        c = Counter(0, 0, 0)
        statisticNumbersFile = open(statisticNumbersFileName, 'w')
        idSnippetsFile = open(idSnippetsFileName, 'w')
        featuresFile = open(featuresFileName, 'w')
        id = 0
        for subFolder in os.listdir(folder):
            pathFolder = os.path.join(folder, subFolder)
            if os.path.isdir(pathFolder):
                c.incFile()
                for file in os.listdir(pathFolder):
                    path = os.path.join(pathFolder, file)
                    if os.path.isfile(path) and (path.find("Snippets_") != -1) and path.endswith(".kt"):
                        c.incSnippets()
                        f = open(path, 'r')
                        id += 1
                        idSnippetsFile.write(str(id) + "\t" + path)
                        idSnippetsFile.write("\n")

                        featureNumTabs = 0.0
                        featureNumSpaces = 0.0
                        featureNumEmptyLines = 0.0
                        featureWhiteSpaceRatio = 0.0
                        featureNumTabsLeadLines = 0.0
                        featureAvgLineLength = 0.0
                        
                        featureNumLinesWithVals = 0.0
                        featureNumLinesWithVars = 0.0
                        featureNumLinesWithEquals = 0.0
                        featureNumOpenBrackets = 0.0
                        featureNumCloseBrackets = 0.0
                        featureNumOpenNumCloseBrackets = 0.0

                        numSpaces = 0
                        numTabs = 0
                        numEmptyLines = 0
                        numTabsLeadLines = 0
                        numNewLines = 0
                        lengthWithoutNewLine = 0

                        for line in f:
                            c.incLine()
                            numNewLines += 1
                            for symbol in line:
                                if symbol == ' ':
                                    numSpaces += 1
                                if symbol == '\t':
                                    numTabs += 1
                                if symbol == '{':
                                    featureNumOpenBrackets += 1.0
                                if symbol == '}':
                                    featureNumCloseBrackets += 1.0
                                if symbol == '=':
                                    featureNumLinesWithEquals += 1.0
                            if "val" in line:
                                featureNumLinesWithVals += 1.0
                            if "var" in line:
                                featureNumLinesWithVars += 1.0
                            itLength = len(line)
                            lengthWithoutNewLine += itLength
                            if itLength > 0:
                                if line[0] == ' ' or line[0] == '\t':
                                    numTabsLeadLines += 1
                            if itLength == 0:
                                numEmptyLines += 1
                        length = lengthWithoutNewLine + numNewLines
                        whiteSpaceRatio = numSpaces + numTabs + numNewLines

                        if numTabs == 0 or length <= 0:
                            featureNumTabs = 0.0
                        else:
                            featureNumTabs = math.log(numTabs / length)


                        if numSpaces == 0 or length <= 0:
                            featureNumSpaces = 0.0
                        else:
                            featureNumSpaces = math.log(numSpaces / length)

                        if numEmptyLines == 0 or length <= 0:
                            featureNumEmptyLines = 0.0
                        else:
                            featureNumEmptyLines = math.log(numEmptyLines / length)

                        if length <= whiteSpaceRatio:
                            featureWhiteSpaceRatio = 0.0
                        else:
                            featureWhiteSpaceRatio = math.log(whiteSpaceRatio / (length - whiteSpaceRatio))

                        if numTabsLeadLines * 2 >= numNewLines:
                            featureNumTabsLeadLines = 1.0
                        else:
                            featureNumTabsLeadLines = 0.0

                        if numNewLines <= 0:
                            featureAvgLineLength = 0.0
                        else:
                            featureAvgLineLength = length / numNewLines
                            
                        if featureNumOpenBrackets == featureNumCloseBrackets:
                            featureNumOpenNumCloseBrackets = 1.0
                        else:
                            featureNumOpenNumCloseBrackets = 0.0

                        featuresList = [ featureNumTabs, featureNumSpaces, featureNumEmptyLines,
                                         featureWhiteSpaceRatio, featureNumTabsLeadLines, featureAvgLineLength,
                                         featureNumLinesWithVals, featureNumLinesWithVars, featureNumLinesWithEquals,
                                         featureNumOpenBrackets, featureNumCloseBrackets, featureNumOpenNumCloseBrackets ]

                        featuresFile.write(str(id))

                        # for featureFromPSI in featuresFromPSIList:
                        #    featuresList.append(featureFromPSI)

                        for feature in featuresList:
                            featuresFile.write("\t" + str(feature))
                        featuresFile.write("\n")

        statisticNumbersFile.write("Files = " + str(c.getFiles()))
        statisticNumbersFile.write("\n")
        statisticNumbersFile.write("Lines = " + str(c.getLines()))
        statisticNumbersFile.write("\n")
        statisticNumbersFile.write("Snippets = " + str(c.getSnippets()))
        statisticNumbersFile.write("\n")

        featuresFile.close()
        idSnippetsFile.close()
        statisticNumbersFile.close()
    except:
        pass

feature_extractor_sourcecode_snippets()

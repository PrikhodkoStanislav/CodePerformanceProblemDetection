import math
import os

folder = "Files"
#folder = "FilesSourcesFromGithub_Snippets_2"
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

def normalized(featureNumLines, length):
    if featureNumLines < 0.1 or length <= 0:
        result = 0.0
    else:
        result = math.log(featureNumLines / length)
    return result

def feature_extractor_sourcecode_snippets():
    try:
        c = Counter(0, 0, 0)
        statisticNumbersFile = open(statisticNumbersFileName, 'w')
        idSnippetsFile = open(idSnippetsFileName, 'w')
        featuresFile = open(featuresFileName, 'w')
        id = 0
        print(folder)
        print(os.getcwd())
        print(os.listdir(folder))
        for subFolder in os.listdir(folder):
            #print(subFolder.path())
            pathFolder = os.path.join(folder, subFolder)
            #print(pathFolder.path())
            print(os.path.isdir(pathFolder))
            if os.path.isdir(pathFolder):
                c.incFile()
                for file in os.listdir(pathFolder):
                    path = os.path.join(pathFolder, file)
                    print(path)
                    if os.path.isfile(path) and (path.find("Snippets_") != -1) and path.endswith(".kt"):
                        c.incSnippets()
                        f = open(path, 'r')
                        id += 1
                        idSnippetsFile.write(str(id) + "\t" + path)
                        idSnippetsFile.write("\n")

                        featureNumTabs = 0.0
                        featureNumTabsNormalized = 0.0

                        featureNumSpaces = 0.0
                        featureNumSpacesNormalized = 0.0

                        featureNumEmptyLines = 0.0
                        featureNumEmptyLinesNormalized = 0.0

                        featureWhiteSpace = 0.0
                        featureNotWhiteSpace = 0.0
                        featureWhiteSpaceRatio = 0.0

                        featureNumTabsLeadLines = 0.0
                        featureNumTabsLeadLinesBool = 0.0

                        featureAvgLineLength = 0.0

                        featureNumOpenBrackets = 0.0

                        featureNumCloseBrackets = 0.0

                        featureNumSlashPlusStar = 0.0

                        featureNumStarPlusSlash = 0.0

                        numEmptyLines = 0.0
                        numTabsLeadLines = 0.0
                        numNewLines = 0.0
                        lengthWithoutNewLine = 0.0

                        featuresWords = ["val ", "var ", "==", "=", "!=", " = ", "{", "}",
                                         "while ", "for ", "if ", "else", ":", "//", "/*", "*/", "continue",
                                         "break", "(", ")", "as", "as?", "class", "do", "true", "false",
                                         "fun", "in", "!in", "interface", "is", "!is", "null", "object"]

                        featuresCounts = (0.0) * len(featuresWords)

                        featuresWordsWithCounts = zip(featuresWords, featuresCounts, featuresCounts, featuresCounts)

                        for line in f:
                            c.incLine()
                            numNewLines += 1.0

                            featureNumTabs += float(line.count("\t"))
                            featureNumSpaces += float(line.count(" "))

                            featureNumSlashPlusStar += float(line.count("/*"))

                            featureNumStarPlusSlash += float(line.count("*/"))

                            if (featureNumSlashPlusStar - featureNumStarPlusSlash) < 0.1:
                                featureSlashPlusStarEqualsStarPlusSlash = 1.0
                            else:
                                featureSlashPlusStarEqualsStarPlusSlash = 0.0

                            for (feature, count1, count2, count3) in featuresWordsWithCounts:
                                count1 += float(line.count(feature))
                                if feature in line:
                                    count2 += 1.0

                            itLength = len(line)
                            lengthWithoutNewLine += float(itLength)
                            if itLength > 0.1:
                                if line[0] == ' ' or line[0] == '\t':
                                    numTabsLeadLines += 1.0
                            if itLength < 0.1:
                                numEmptyLines += 1.0
                        length = lengthWithoutNewLine + numNewLines
                        whiteSpaceRatio = featureNumTabs + featureNumSpaces + numNewLines

                        featureNumTabsNormalized = normalized(featureNumTabs, length)
                        featureNumSpacesNormalized = normalized(featureNumSpaces, length)

                        featureNumEmptyLines = float(numEmptyLines)
                        if numEmptyLines < 0.1 or length <= 0:
                            featureNumEmptyLinesNormalized = 0.0
                        else:
                            featureNumEmptyLinesNormalized = math.log(numEmptyLines / length)

                        featureWhiteSpace = whiteSpaceRatio
                        featureNotWhiteSpace = length - whiteSpaceRatio
                        if length <= whiteSpaceRatio:
                            featureWhiteSpaceRatio = 0.0
                        else:
                            featureWhiteSpaceRatio = math.log(whiteSpaceRatio / (length - whiteSpaceRatio))

                        featureNumTabsLeadLines = numTabsLeadLines
                        if numTabsLeadLines * 2 >= numNewLines:
                            featureNumTabsLeadLinesBool = 1.0
                        else:
                            featureNumTabsLeadLinesBool = 0.0

                        if numNewLines <= 0:
                            featureAvgLineLength = 0.0
                        else:
                            featureAvgLineLength = length / numNewLines
                            
                        if (featureNumOpenBrackets - featureNumCloseBrackets) < 0.1:
                            featureNumOpenNumCloseBrackets = 1.0
                        else:
                            featureNumOpenNumCloseBrackets = 0.0

                        for (feature, count1, count2, count3) in featuresWordsWithCounts:
                            count3 = normalized(count2, length)

                        featuresList = []
                        for (feature, count1, count2, count3) in featuresWordsWithCounts:
                            featuresList.append([count1, count2, count3])

                        featuresList.append([featureNumTabs, featureNumTabsNormalized, featureNumSpaces,
                                             featureNumSpacesNormalized, featureNumEmptyLines, featureNumEmptyLinesNormalized,
                                             featureWhiteSpace, featureNotWhiteSpace, featureWhiteSpaceRatio, featureNumTabsLeadLines,
                                             featureNumTabsLeadLinesBool, featureAvgLineLength, featureNumOpenNumCloseBrackets,
                                             featureSlashPlusStarEqualsStarPlusSlash])

                        featuresFile.write(str(id))

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
        #print('fff')
        pass

feature_extractor_sourcecode_snippets()

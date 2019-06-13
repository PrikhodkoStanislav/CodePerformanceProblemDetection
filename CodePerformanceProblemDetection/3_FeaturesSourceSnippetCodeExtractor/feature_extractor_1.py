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

                        featureNumLinesWithVals = 0.0
                        featureNumLinesWithValsNormalized = 0.0
                        featureNumVals = 0.0

                        featureNumLinesWithVars = 0.0
                        featureNumLinesWithVarsNormalized = 0.0
                        featureNumVars = 0.0

                        featureNumLinesWithOneEqual = 0.0
                        featureNumLinesWithOneEqualNormalized = 0.0
                        featureNumOneEqual = 0.0

                        featureNumOpenBrackets = 0.0
                        featureNumLinesWithOpenBrackets = 0.0
                        featureNumLinesWithOpenBracketsNormalized = 0.0

                        featureNumCloseBrackets = 0.0
                        featureNumLinesWithCloseBrackets = 0.0
                        featureNumLinesWithCloseBracketsNormalized = 0.0

                        featureNumOpenNumCloseBrackets = 0.0

                        featureNumWhile = 0.0
                        featureNumLinesWithWhile = 0.0
                        featureNumLinesWithWhileNormalized = 0.0

                        featureNumFor = 0.0
                        featureNumLinesWithFor = 0.0
                        featureNumLinesWithForNormalized = 0.0

                        featureNumIf = 0.0
                        featureNumLinesWithIf = 0.0
                        featureNumLinesWithIfNormalized = 0.0

                        featureNumElse = 0.0
                        featureNumLinesWithElse = 0.0
                        featureNumLinesWithElseNormalized = 0.0

                        featureNumPoints = 0.0
                        featureNumLinesWithPoints = 0.0
                        featureNumLinesWithPointsNormalized = 0.0

                        featureNumSlashs = 0.0
                        featureNumLinesWithSlashs = 0.0
                        featureNumLinesWithSlashsNormalized = 0.0

                        featureNumSlashPlusStar = 0.0
                        featureNumLinesWithSlashPlusStar = 0.0
                        featureNumLinesWithSlashPlusStarNormalized = 0.0

                        featureNumStarPlusSlash = 0.0
                        featureNumLinesWithStarPlusSlash = 0.0
                        featureNumLinesWithStarPlusSlashNormalized = 0.0

                        featureSlashPlusStarEqualsStarPlusSlash = 0.0

                        featureNumEquals = 0.0
                        featureNumLinesWithEquals = 0.0
                        featureNumLinesWithEqualsNormalized = 0.0

                        featureNumNotEquals = 0.0
                        featureNumLinesWithNotEquals = 0.0
                        featureNumLinesWithNotEqualsNormalized = 0.0

                        featureNumIs = 0.0
                        featureNumLinesWithIs = 0.0
                        featureNumLinesWithIsNormalized = 0.0

                        featureNumContinue = 0.0
                        featureNumLinesWithContinue = 0.0
                        featureNumLinesWithContinueNormalized = 0.0

                        featureNumBreak = 0.0
                        featureNumLinesWithBreak = 0.0
                        featureNumLinesWithBreakNormalized = 0.0

                        featureNumOBrackets = 0.0
                        featureNumLinesWithOBrackets = 0.0
                        featureNumLinesWithOBracketsNormalized = 0.0

                        featureNumCBrackets = 0.0
                        featureNumLinesWithCBrackets = 0.0
                        featureNumLinesWithCBracketsNormalized = 0.0

                        featureNumAs = 0.0
                        featureNumLinesWithAs = 0.0
                        featureNumLinesWithAsNormalized = 0.0

                        featureNumAsSafe = 0.0
                        featureNumLinesWithAsSafe = 0.0
                        featureNumLinesWithAsSafeNormalized = 0.0

                        featureNumClass = 0.0
                        featureNumLinesWithClass = 0.0
                        featureNumLinesWithClassNormalized = 0.0

                        featureNumDo = 0.0
                        featureNumLinesWithDo = 0.0
                        featureNumLinesWithDoNormalized = 0.0

                        featureNumTrue = 0.0
                        featureNumLinesWithTrue = 0.0
                        featureNumLinesWithTrueNormalized = 0.0

                        featureNumFalse = 0.0
                        featureNumLinesWithFalse = 0.0
                        featureNumLinesWithFalseNormalized = 0.0

                        featureNumFun = 0.0
                        featureNumLinesWithFun = 0.0
                        featureNumLinesWithFunNormalized = 0.0

                        featureNumIn = 0.0
                        featureNumLinesWithIn = 0.0
                        featureNumLinesWithInNormalized = 0.0

                        featureNumInExclamation = 0.0
                        featureNumLinesWithInExclamation = 0.0
                        featureNumLinesWithInExclamationNormalized = 0.0

                        featureNumInterface = 0.0
                        featureNumLinesWithInterface = 0.0
                        featureNumLinesWithInterfaceNormalized = 0.0

                        featureNumWordIs = 0.0
                        featureNumLinesWithWordIs = 0.0
                        featureNumLinesWithWordIsNormalized = 0.0

                        featureNumWordIsExclamation = 0.0
                        featureNumLinesWithWordIsExclamation = 0.0
                        featureNumLinesWithWordIsExclamationNormalized = 0.0

                        featureNumNull = 0.0
                        featureNumLinesWithNull = 0.0
                        featureNumLinesWithNullNormalized = 0.0

                        featureNumObject = 0.0
                        featureNumLinesWithObject= 0.0
                        featureNumLinesWithObjectNormalized = 0.0


                        numEmptyLines = 0.0
                        numTabsLeadLines = 0.0
                        numNewLines = 0.0
                        lengthWithoutNewLine = 0.0


                        for line in f:
                            c.incLine()
                            numNewLines += 1.0

                            featureNumTabs += float(line.count("\t"))
                            featureNumSpaces += float(line.count(" "))

                            featureNumVals += float(line.count("val "))
                            if "val " in line:
                                featureNumLinesWithVals += 1.0

                            featureNumVars += float(line.count("var "))
                            if "var " in line:
                                featureNumLinesWithVars += 1.0

                            featureNumEquals += float(line.count("=="))
                            if "==" in line:
                                featureNumLinesWithEquals += 1.0

                            featureNumOneEqual += float(line.count("="))
                            if "=" in line:
                                featureNumLinesWithOneEqual += 1.0

                            featureNumNotEquals += float(line.count("!="))
                            if "!=" in line:
                                featureNumLinesWithNotEquals += 1.0

                            featureNumIs += float(line.count(" = "))
                            if " = " in line:
                                featureNumLinesWithIs += 1.0

                            featureNumOpenBrackets += float(line.count("{"))
                            if "{" in line:
                                featureNumLinesWithOpenBrackets += 1.0

                            featureNumCloseBrackets += float(line.count("}"))
                            if "}" in line:
                                featureNumLinesWithCloseBrackets += 1.0

                            featureNumWhile += float(line.count("while "))
                            if "while " in line:
                                featureNumLinesWithWhile += 1.0

                            featureNumFor += float(line.count("for "))
                            if "for " in line:
                                featureNumLinesWithFor += 1.0

                            featureNumIf += float(line.count("if "))
                            if "if " in line:
                                featureNumLinesWithIf += 1.0

                            featureNumElse += float(line.count("else"))
                            if "else" in line:
                                featureNumLinesWithElse += 1.0

                            featureNumPoints += float(line.count(":"))
                            if ":" in line:
                                featureNumLinesWithPoints += 1.0

                            featureNumSlashs += float(line.count("//"))
                            if "//" in line:
                                featureNumLinesWithSlashs += 1.0

                            featureNumSlashPlusStar += float(line.count("/*"))
                            if "/*" in line:
                                featureNumLinesWithSlashPlusStar += 1.0

                            featureNumStarPlusSlash += float(line.count("*/"))
                            if "*/" in line:
                                featureNumLinesWithStarPlusSlash += 1.0

                            if (featureNumSlashPlusStar - featureNumStarPlusSlash) < 0.1:
                                featureSlashPlusStarEqualsStarPlusSlash = 1.0
                            else:
                                featureSlashPlusStarEqualsStarPlusSlash = 0.0

                            featureNumContinue += float(line.count("continue"))
                            if "continue" in line:
                                featureNumLinesWithContinue += 1.0

                            featureNumBreak += float(line.count("break"))
                            if "break" in line:
                                featureNumLinesWithBreak += 1.0

                            featureNumOBrackets += float(line.count("("))
                            if "(" in line:
                                featureNumLinesWithOBrackets += 1.0

                            featureNumCBrackets += float(line.count(")"))
                            if ")" in line:
                                featureNumLinesWithCBrackets += 1.0

                            featureNumAs += float(line.count("as"))
                            if "as" in line:
                                featureNumLinesWithAs += 1.0

                            featureNumAsSafe += float(line.count("as?"))
                            if "as?" in line:
                                featureNumLinesWithAsSafe += 1.0

                            featureNumClass += float(line.count("class"))
                            if "class" in line:
                                featureNumLinesWithClass += 1.0

                            featureNumDo += float(line.count("do"))
                            if "do" in line:
                                featureNumLinesWithDo += 1.0

                            featureNumTrue += float(line.count("true"))
                            if "true" in line:
                                featureNumLinesWithTrue += 1.0

                            featureNumFalse += float(line.count("false"))
                            if "false" in line:
                                featureNumLinesWithFalse += 1.0

                            featureNumFun += float(line.count("fun"))
                            if "fun" in line:
                                featureNumLinesWithFun += 1.0

                            featureNumIn += float(line.count("in"))
                            if "in" in line:
                                featureNumLinesWithIn += 1.0

                            featureNumInExclamation += float(line.count("!in"))
                            if "!in" in line:
                                featureNumLinesWithInExclamation += 1.0

                            featureNumInterface += float(line.count("interface"))
                            if "interface" in line:
                                featureNumLinesWithInterface += 1.0

                            featureNumWordIs += float(line.count("is"))
                            if "is" in line:
                                featureNumLinesWithWordIs += 1.0

                            featureNumWordIsExclamation += float(line.count("!is"))
                            if "!is" in line:
                                featureNumLinesWithWordIsExclamation += 1.0

                            featureNumNull += float(line.count("null"))
                            if "null" in line:
                                featureNumLinesWithNull += 1.0

                            featureNumObject += float(line.count("object"))
                            if "object" in line:
                                featureNumLinesWithObject += 1.0


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

                        featureNumLinesWithValsNormalized = normalized(featureNumLinesWithVals, length)
                        featureNumLinesWithVarsNormalized = normalized(featureNumLinesWithVars, length)
                        featureNumLinesWithEqualsNormalized = normalized(featureNumLinesWithEquals, length)
                        featureNumLinesWithOneEqualNormalized = normalized(featureNumLinesWithOneEqual, length)
                        featureNumLinesWithNotEqualsNormalized = normalized(featureNumLinesWithNotEquals, length)
                        featureNumLinesWithIsNormalized = normalized(featureNumLinesWithIs, length)
                        featureNumLinesWithOpenBracketsNormalized = normalized(featureNumLinesWithOpenBrackets, length)
                        featureNumLinesWithCloseBracketsNormalized = normalized(featureNumLinesWithCloseBrackets, length)
                        featureNumLinesWithWhileNormalized = normalized(featureNumLinesWithWhile, length)
                        featureNumLinesWithForNormalized = normalized(featureNumLinesWithFor, length)
                        featureNumLinesWithIfNormalized = normalized(featureNumLinesWithIf, length)
                        featureNumLinesWithElseNormalized = normalized(featureNumLinesWithElse, length)
                        featureNumLinesWithPointsNormalized = normalized(featureNumLinesWithPoints, length)
                        featureNumLinesWithSlashsNormalized = normalized(featureNumLinesWithSlashs, length)
                        featureNumLinesWithSlashPlusStarNormalized = normalized(featureNumLinesWithSlashPlusStar, length)
                        featureNumLinesWithStarPlusSlashNormalized = normalized(featureNumLinesWithStarPlusSlash, length)
                        featureNumLinesWithContinueNormalized = normalized(featureNumLinesWithContinue, length)
                        featureNumLinesWithBreakNormalized = normalized(featureNumLinesWithBreak, length)
                        featureNumLinesWithOBracketsNormalized = normalized(featureNumLinesWithOBrackets, length)
                        featureNumLinesWithCBracketsNormalized = normalized(featureNumLinesWithCBrackets, length)
                        featureNumLinesWithAsNormalized = normalized(featureNumLinesWithAs, length)
                        featureNumLinesWithAsSafeNormalized = normalized(featureNumLinesWithAsSafe, length)
                        featureNumLinesWithClassNormalized = normalized(featureNumLinesWithClass, length)
                        featureNumLinesWithDoNormalized = normalized(featureNumLinesWithDo, length)
                        featureNumLinesWithTrueNormalized = normalized(featureNumLinesWithTrue, length)
                        featureNumLinesWithFalseNormalized = normalized(featureNumLinesWithFalse, length)
                        featureNumLinesWithFunNormalized = normalized(featureNumLinesWithFun, length)
                        featureNumLinesWithInNormalized = normalized(featureNumLinesWithIn, length)
                        featureNumLinesWithInExclamationNormalized = normalized(featureNumLinesWithInExclamation, length)
                        featureNumLinesWithInterfaceNormalized = normalized(featureNumLinesWithInterface, length)
                        featureNumLinesWithWordIsNormalized = normalized(featureNumLinesWithWordIs, length)
                        featureNumLinesWithWordIsExclamationNormalized = normalized(featureNumLinesWithWordIsExclamation, length)
                        featureNumLinesWithNullNormalized = normalized(featureNumLinesWithNull, length)
                        featureNumLinesWithObjectNormalized = normalized(featureNumLinesWithObject, length)

                        featuresList = [ featureNumTabs, featureNumTabsNormalized, featureNumSpaces, featureNumSpacesNormalized,
                                         featureNumEmptyLines, featureNumEmptyLinesNormalized,
                                         featureWhiteSpace, featureNotWhiteSpace, featureWhiteSpaceRatio, featureNumTabsLeadLines,
                                         featureNumTabsLeadLinesBool, featureAvgLineLength, featureNumOpenNumCloseBrackets,
                                         featureNumLinesWithVals, featureNumLinesWithValsNormalized, featureNumVals,
                                         featureNumLinesWithVars, featureNumLinesWithVarsNormalized, featureNumVars,
                                         featureNumEquals, featureNumLinesWithEquals, featureNumLinesWithEqualsNormalized,
                                         featureNumLinesWithOneEqual, featureNumLinesWithOneEqualNormalized, featureNumOneEqual,
                                         featureNumNotEquals, featureNumLinesWithNotEquals, featureNumLinesWithNotEqualsNormalized,
                                         featureNumIs, featureNumLinesWithIs, featureNumLinesWithIsNormalized,
                                         featureNumOpenBrackets, featureNumLinesWithOpenBrackets, featureNumLinesWithOpenBracketsNormalized,
                                         featureNumCloseBrackets, featureNumLinesWithCloseBrackets, featureNumLinesWithCloseBracketsNormalized,
                                         featureNumWhile, featureNumLinesWithWhile, featureNumLinesWithWhileNormalized,
                                         featureNumFor, featureNumLinesWithFor, featureNumLinesWithForNormalized,
                                         featureNumIf, featureNumLinesWithIf, featureNumLinesWithIfNormalized,
                                         featureNumElse, featureNumLinesWithElse, featureNumLinesWithElseNormalized,
                                         featureNumPoints, featureNumLinesWithPoints, featureNumLinesWithPointsNormalized,
                                         featureNumSlashs, featureNumLinesWithSlashs, featureNumLinesWithSlashsNormalized,
                                         featureNumSlashPlusStar, featureNumLinesWithSlashPlusStar, featureNumLinesWithSlashPlusStarNormalized,
                                         featureNumStarPlusSlash, featureNumLinesWithStarPlusSlash, featureNumLinesWithStarPlusSlashNormalized,
                                         featureSlashPlusStarEqualsStarPlusSlash,
                                         featureNumContinue, featureNumLinesWithContinue, featureNumLinesWithContinueNormalized,
                                         featureNumBreak, featureNumLinesWithBreak, featureNumLinesWithBreakNormalized,
                                         featureNumOBrackets, featureNumLinesWithOBrackets, featureNumLinesWithOBracketsNormalized,
                                         featureNumCBrackets, featureNumLinesWithCBrackets, featureNumLinesWithCBracketsNormalized,
                                         featureNumAs, featureNumLinesWithAs, featureNumLinesWithAsNormalized,
                                         featureNumAsSafe, featureNumLinesWithAsSafe, featureNumLinesWithAsSafeNormalized,
                                         featureNumClass, featureNumLinesWithClass, featureNumLinesWithClassNormalized,
                                         featureNumDo, featureNumLinesWithDo, featureNumLinesWithDoNormalized,
                                         featureNumTrue, featureNumLinesWithTrue, featureNumLinesWithTrueNormalized,
                                         featureNumFalse, featureNumLinesWithFalse, featureNumLinesWithFalseNormalized,
                                         featureNumFun, featureNumLinesWithFun, featureNumLinesWithFunNormalized,
                                         featureNumIn, featureNumLinesWithIn, featureNumLinesWithInNormalized,
                                         featureNumInExclamation, featureNumLinesWithInExclamation, featureNumLinesWithInExclamationNormalized,
                                         featureNumInterface, featureNumLinesWithInterface, featureNumLinesWithInterfaceNormalized,
                                         featureNumWordIs, featureNumLinesWithWordIs, featureNumLinesWithWordIsNormalized,
                                         featureNumWordIsExclamation, featureNumLinesWithWordIsExclamation, featureNumLinesWithWordIsExclamationNormalized,
                                         featureNumNull, featureNumLinesWithNull, featureNumLinesWithNullNormalized,
                                         featureNumObject, featureNumLinesWithObject, featureNumLinesWithObjectNormalized
                                         ]

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
        #print('fff')
        pass

feature_extractor_sourcecode_snippets()

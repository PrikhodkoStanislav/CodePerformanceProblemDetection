import os
import shutil

folder = "FilesSourcesFromGithub"
snipFolder = "Snippets"
snipFolderName = "FilesSourcesFromGithub_Snippets_2"

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

def createSnippets(folder, snipFolder, counter):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".kt"):
            counter.incFile()
            extractSnippets(path, file, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, file, snipFolder, counter)
    return

def createSnippetsDir(folder, repo, snipFolder, counter):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".kt"):
            counter.incFile()
            extractSnippets(path, file, repo, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, repo, snipFolder, counter)
    return

def extractSnippets(path, file, repo, snipFolder, counter):
    newFileName = file[:file.rindex('.')]
    name = snipFolderName + "\\" + repo + "_" + newFileName
    i = 1
    while os.path.exists(name):
        name2 = name + "_" + str(i)
        if os.path.exists(name2):
            i += 1
        else:
            name = name2
    os.mkdir(name)
    snipId = 1
    f = open(path, 'r')
    state = 0
    fileOutput = open(path + "x", 'w')
    numBrackets = 0
    try:
        for line in f:
            counter.incLine()
            if state == 0:
                if line.find("fun") != -1:
                    counter.incSnippets()
                    state = 1
                    fileOutput = open(name + "\\" + snipFolder + "_" + str(snipId) + ".kt", 'w')
                    fileOutput.write(line)
                    fileOutput.write("\n")
                    for c in line:
                        if c == '{':
                            numBrackets += 1
                        elif c == '}':
                            numBrackets -= 1
            else:
                fileOutput.write(line)
                fileOutput.write("\n")
                for c in line:
                    if c == '{':
                        numBrackets += 1
                    elif c == '}':
                        numBrackets -= 1
                if numBrackets == 0:
                    fileOutput.close()
                    snipId += 1
                    state = 0
    except:
        pass
    f.close()

def extractor():
    c = Counter(0, 0, 0)
    if os.path.exists(snipFolderName):
        shutil.rmtree(snipFolderName)
    os.mkdir(snipFolderName)
    createSnippets(folder, snipFolder, c)
    print("Files = " + str(c.getFiles()))
    print("\n")
    print("Lines = " + str(c.getLines()))
    print("\n")
    print("Snippets = " + str(c.getSnippets()))
    print("\n")

extractor()

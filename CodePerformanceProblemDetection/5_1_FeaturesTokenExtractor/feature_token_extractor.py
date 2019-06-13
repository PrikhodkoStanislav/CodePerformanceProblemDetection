import os

folder = "C:/cppd/D/CodePerformanceProblemDetection/5_1_FeaturesTokenExtractor/data"

featuresFileName = "featuresPSI.tsv"
statisticNumbersFileName = "statisticsPSI.txt"

snipFolder = ""

tokens = []

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

def feature_extractor_token():
    counter = Counter(0, 0, 0)
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        #path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".txt"):
            counter.incFile()
            extractTokenList(path, file, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, file, snipFolder, counter)
    print(tokens)
    print(len(tokens))
    print(counter.getFiles())
    return

def createSnippetsDir(folder, repo, snipFolder, counter):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        #path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".txt"):
            counter.incFile()
            extractTokenList(path, file, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, repo, snipFolder, counter)
    return

def extractTokenList(path, file, snipFolder, counter):
    f = open(path, 'r')
    token_types = [line.split(' (')[0] for line in f]
    print(token_types)
    for t in token_types:
        if t not in tokens:
            tokens.append(t)

feature_extractor_token()
import os

folder = "FilesSourcesFromGithub"

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

def feature_extractor_token():
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        #path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".txt"):
            counter.incFile()
            extractSnippets(path, file, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, file, snipFolder, counter)
    return

def feature_extractor_token():
    
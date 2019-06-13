import os
#folder = "C:/cppd/D/CodePerformanceProblemDetection/5_1_FeaturesTokenExtractor/data"
#folder = "D:/Project/CodePerformanceProblemDetection/5_1_FeaturesTokenExtractor/data"
folder = "D:/Project/New_Project/Dataset/New_Dataset in folders"

path_log = "D:/Project/CodePerformanceProblemDetection/5_1_FeaturesTokenExtractor/log.txt"

featuresFileName = "featuresPSI.tsv"
statisticNumbersFileName = "statisticsPSI.txt"

snipFolder = ""

tokens = []

token_matrix = []

files_list = []
token_list = []
value_list = []

value_matrix = []
value_files_list = []

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
        #path = folder + "/" + file
        #path.replace(' ', '_')
        if os.path.isfile(path) and path.endswith(".txt"):
            counter.incFile()
            extractTokenList(path, file, snipFolder, counter)
        elif os.path.isdir(path):
            createSnippetsDir(path, file, snipFolder, counter)
    #print(token_matrix)
    #print(tokens)
    #print(len(tokens))
    #print(counter.getFiles())
    return

def createSnippetsDir(folder, repo, snipFolder, counter):
    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            #path = folder + "/" + file
            #path.replace(' ', '_')
            if os.path.isfile(path) and path.endswith(".txt"):
                counter.incFile()
                extractTokenList(path, file, snipFolder, counter)
            elif os.path.isdir(path):
                createSnippetsDir(path, repo, snipFolder, counter)
    except:
        with open('bad_files.txt', 'w') as f:
            f.write(folder + "/" + file)
            f.write("\n")
        pass
    return

import codecs
import csv

def extractTokenList(path, file, snipFolder, counter):
    #f = open(path, 'r')
    f = codecs.open(path, "r", "utf_8_sig" )
    #fileOutput = open(path_log, 'w')
    #fileOutput.write(path)
    #fileOutput.write("\n")
    #fileOutput.close()
    token_types = []
    value_types = []
    for line in f:
        token_types.append(line.split(' (')[0])
        value_types.append(line.split(' (', 1)[1].rsplit(')', 1)[0])
    #token_types = [line.split(' (')[0] for line in f]
    #value_types = [(line.split(' (\'', 1)[1]).rsplit('\')', 1)[0] for line in f]
    #token_types = [split_unicode_chrs(line)[0] for line in f]
    #token_matrix.append(token_types)
    files_list.append(path)
    #value_matrix.append(value_types)
    #value_files_list.append(path)
    with open(path + ".token", 'w') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter=' ', lineterminator='\n')
        tsv_writer.writerow(token_types)
    with open(path + ".value", 'w') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter=' ', lineterminator='\n')
        tsv_writer.writerow(value_types)

feature_extractor_token()

token_list = list(map(lambda x: x + ".token", files_list))
value_list = list(map(lambda x: x + ".value", files_list))

import pickle

class DataFilePath:
    def __setitem__(self, index: int, value):
        '''сохранить в файл index.data'''
        with open('{}.data'.format(index), 'wb') as f:
            pickle.dump(value, f)

    def __getitem__(self, index: int):
        '''читать из файла index.data'''
        with open('{}.data'.format(index), 'rb') as f:
            return pickle.load(f)

file = DataFilePath()

file[10] = token_list
file[11] = value_list

d1 = file[10]
#print(d1)

import argparse
import codecs
import csv
import math
import os
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--folder', '-f', nargs=1, type=str, help='input folder with token types in .token format')
parser.add_argument('--output', '-o', nargs=1, type=str, help='output folder with vectors for token types in .tsv format')
args = parser.parse_args()

folder_for_token_types_list = args.folder[0]
folder_for_token_vector = args.output[0]

bad_files_step_1 = folder_for_token_vector + "/bad_files_step_1.txt"

token_types = []
token_number_docs = defaultdict(int)

end_name = ".token"

f_b = open(bad_files_step_1, "w")

def visit_folder(folder):
    for file in os.listdir(folder):
        path = folder + "/" + file
        try:
            if os.path.isfile(path) and path.endswith(end_name):
                extract_info(path)
            elif os.path.isdir(path):
                visit_folder(path)
        except:
            f_b.write(path + "\n")

def extract_info(path):
    try:
        f = codecs.open(path, "r", "utf_8_sig")
        s = set()
        for line in f:
            tokens = line.split(" ")
            for t in tokens:
                s.add(t)
        for s_t in s:
            if s_t not in token_types:
                token_types.append(s_t)
            token_number_docs[s_t] += 1
    except:
        f_b.write("=====\n" + path + "\n=====\n")

for file in os.listdir(folder_for_token_types_list):
    path = folder_for_token_types_list + "/" + file
    try:
        if os.path.isfile(path) and path.endswith(end_name):
            extract_info(path)
        elif os.path.isdir(path):
            visit_folder(path)
    except:
        f_b.write(path + "\n")

f_b.close()

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

data_file = DataFilePath()

data_file[0] = token_types
data_file[1] = token_number_docs

vector_file = folder_for_token_vector + "/vector_token.tsv"

file_vector = open(vector_file, 'w')

tsv_writer = csv.writer(file_vector, delimiter='\t', lineterminator='\n')

res_names = []
for t_t in token_types:
    res_names.append("count_" + t_t)
    res_names.append("bin_" + t_t)
    res_names.append("tf_" + t_t)
    res_names.append("idf_" + t_t)
    res_names.append("tfidf_" + t_t)
tsv_writer.writerow(["ID", "Path"] + res_names)

bad_files_step_2 = folder_for_token_vector + "/bad_files_step_2.txt"

f_b_2 = open(bad_files_step_2, "w")

id_num = 1

def visit_folder_2(folder):
    for file in os.listdir(folder):
        path = folder + "/" + file
        try:
            if os.path.isfile(path) and path.endswith(end_name):
                extract_info_2(path)
            elif os.path.isdir(path):
                visit_folder_2(path)
        except:
            f_b_2.write(path + "\n")

def extract_info_2(path):
    global id_num
    try:
        f = open(path, "r")
        token_count = defaultdict(int)
        vec = []
        k = 0
        for line in f:
            tokens = line.split(" ")
            k += len(tokens)
            for t in tokens:
                token_count[t] += 1
        for t_t in token_types:
            c = token_count[t_t]
            vec.append(c)
            if c > 0:
                vec.append(1)
            else:
                vec.append(0)
            tf = 0
            if k > 0:
                tf = c / k
            idf = 0
            if token_number_docs[c] > 0:
                idf = log(c / token_number_docs[c])
            tf_idf = tf * idf
            vec.append(tf)
            vec.append(idf)
            vec.append(tf_idf)
        tsv_writer.writerow([id_num] + [path] + vec)
        id_num += 1
    except Exception as e:
        f_b_2.write(str(e) + "\n")
        f_b_2.write("=====\n" + path + "\n=====\n")

for file in os.listdir(folder_for_token_vector):
    path = folder_for_token_vector + "/" + file
    try:
        if os.path.isfile(path) and path.endswith(end_name):
            extract_info_2(path)
        elif os.path.isdir(path):
            visit_folder_2(path)
    except:
        f_b_2.write(path + "\n")

f_b_2.close()

file_vector.close()

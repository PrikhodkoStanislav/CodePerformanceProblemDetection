import argparse
import codecs
import csv
import math
import os
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--folder', '-f', nargs=1, type=str, help='input folder with lexems in .value format')
parser.add_argument('--output', '-o', nargs=1, type=str, help='output folder with vectors for lexems in .tsv format')
args = parser.parse_args()

folder_for_value_list = args.folder[0]
folder_for_value_vector = args.output[0]

token_types = []

end_name = ".value"
end_token_name = ".token"

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

token_types = data_file[0]

vector_file = folder_for_value_vector + "/vector_value.tsv"

file_vector = open(vector_file, 'w')

tsv_writer = csv.writer(file_vector, delimiter='\t', lineterminator='\n')

res_names = []
res_names.append("sum_len_")
for t_t in token_types:
    res_names.append("bin_" + t_t)
    res_names.append("len_" + t_t)
    res_names.append("tf_len_" + t_t)
    res_names.append("log_tf_len_" + t_t)
    res_names.append("hash_" + t_t)
    res_names.append("tf_hash_" + t_t)
    res_names.append("log_tf_hash_" + t_t)
tsv_writer.writerow(["ID", "Path"] + res_names)

bad_files_value = folder_for_value_vector + "/bad_files_value.txt"

f_b_v = open(bad_files_value, "w")

special_files_value = folder_for_value_vector + "/special_files_value.txt"

s_f_v = open(special_files_value, "w")

id_num = 1

def visit_folder_2(folder):
    for file in os.listdir(folder):
        path = folder + "/" + file
        try:
            if os.path.isfile(path) and path.endswith(end_name):
                extract_info_2(path)
            elif os.path.isdir(path):
                visit_folder_2(path)
        except Exception as e:
            f_b_v.write(str(e) + "\n")
            f_b_v.write(path + "\n")

def extract_info_2(path):
    global id_num
    try:
        f = open(path, "r")
        len_token = 0
        len_value = 0
        token_file_path = path.replace(end_name, end_token_name)
        try:
            f_t = open(token_file_path, "r")
            for line in f_t:
                tokens = line.split(" ")
                len_token += len(tokens)
        except Exception as e:
            f_b_v.write("=====\n" + str(e) + "\n")
            f_b_v.write(token_file_path + "\n=====\n")
            return
        value_len_count = defaultdict(int)
        value_hash_count = defaultdict(int)
        vec = []
        sum = 0
        sum_h = 0
        for line in f:
            values = re.findall("'.+?'", line)
            len_value += len(values)
            if len_value != len_token:
                s_f_v.write(path + "\n")
                return
            for cou in range(0, len_value):
                value_len_count[tokens[cou]] += len(values[cou])
                value_hash_count[tokens[cou]] += hash(values[cou])
                sum += len(values[cou])
                sum_h += hash(values[cou])
        vec.append(sum)
        for t_t in token_types:
            vlc = value_len_count[t_t]
            if vlc > 0:
                vec.append(1)
            else:
                vec.append(0)
            vec.append(vlc)
            if sum > 0:
                vec.append(vlc / sum)
            else:
                vec.append(0)
            if sum > 0 and vlc > 0:
                vec.append(math.log(vlc / sum))
            else:
                vec.append(0)
            vhc = value_hash_count[t_t]
            vec.append(vhc)
            if sum_h > 0:
                vec.append(vhc / sum_h)
            else:
                vec.append(0)
            if sum_h > 0 and vhc > 0:
                vec.append(math.log(vhc / sum_h))
            else:
                vec.append(0)
        tsv_writer.writerow([id_num] + [path] + vec)
        id_num += 1
    except Exception as e:
        f_b_v.write(str(e) + "\n")
        f_b_v.write("=====\n" + path + "\n=====\n")

for file in os.listdir(folder_for_value_vector):
    path = folder_for_value_vector + "/" + file
    try:
        if os.path.isfile(path) and path.endswith(end_name):
            extract_info_2(path)
        elif os.path.isdir(path):
            visit_folder_2(path)
    except Exception as e:
        f_b_v.write(str(e) + "\n")
        f_b_v.write(path + "\n")

f_b_v.close()

file_vector.close()


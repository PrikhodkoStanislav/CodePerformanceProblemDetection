import argparse
import codecs
import csv
import getopt
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--folder', '-f', nargs=1, type=str, help='input folder with tokens in txt format')
args = parser.parse_args()

folder = args.folder[0]

def extract_tokens(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path) and path.endswith(".txt"):
            extract_token_list(path)
        elif os.path.isdir(path):
            extract_tokens(path)
    return

def extract_token_list(path):
    f = codecs.open(path, "r", "utf_8_sig")
    token_types = []
    value_types = []
    for line in f:
        token_types.append(line.split(' (')[0])
        value_types.append(line.split(' (', 1)[1].rsplit(')', 1)[0])
    with open(path + ".token", 'w') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter=' ', lineterminator='\n')
        tsv_writer.writerow(token_types)
    with open(path + ".value", 'w') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter=' ', lineterminator='\n')
        tsv_writer.writerow(value_types)

extract_tokens(folder)

import argparse
import os
import pandas as pd
import shutil
from sklearn.cluster import KMeans

parser = argparse.ArgumentParser()
parser.add_argument('--folder', '-f', nargs=1, type=str, help='input folder with features from vector in .tsv format')
parser.add_argument('--output', '-o', nargs=1, type=str, help='output folder with folders with code groups')
args = parser.parse_args()

features_path = args.folder[0] + 'vector_token.tsv'
folder = args.output[0]

df=pd.read_csv(features_path, header=0, sep='\t', encoding = "ISO-8859-1")

feature_vectors = df.values[:,2:]

paths_to_sources = df.values[:,1:2]
filenames_list = []
for t_t in paths_to_sources:
  for i in t_t:
    filenames_list.append(str(i))

kmeans = KMeans(n_clusters=23).fit(feature_vectors)
labels = kmeans.labels_

k = 0
for i in labels:
    token_filename = filenames_list[k].split('/', 6)[5]
    filename = token_filename.replace(".txt.token", ".kt")
    source_path = filenames_list[k].replace(".txt.token", ".kt")
    folder_name = folder + str(i)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    shutil.copyfile(source_path, folder_name + "/" + filename)
    k += 1


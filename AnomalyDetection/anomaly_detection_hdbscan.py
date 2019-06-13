import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', nargs=1, type=str, help='input file with features from vector in .tsv format')
parser.add_argument('--output', '-o', nargs=1, type=str, help='output file with outliers in .tsv format')
args = parser.parse_args()

file_with_features = args.input[0]
file_with_outliers = args.output[0]

import pandas as pd
features_path = file_with_features
df=pd.read_csv(features_path, header=0, sep='\t', encoding = "ISO-8859-1")
import numpy as np
X = np.array(df.values[:,2:])
print(X.shape)
from sklearn.preprocessing import scale
X = scale(X)

num = X.shape[0]
import hdbscan
import time

def parse_timediff(timediff):
    h = timediff // 3600
    m = timediff % 3600 // 60
    s = timediff % 60
    return h, m, s

local_start = time.time()

clusterer = hdbscan.HDBSCAN(min_cluster_size=15).fit(X)

hours, minutes, seconds = parse_timediff(time.time() - local_start)

print(hours)
print(minutes)
print(seconds)

clusterer.outlier_scores_
print(clusterer.outlier_scores_)

threshold = 0.95
outliers = np.where(clusterer.outlier_scores_ > threshold)

outliers_file_name = file_with_outliers

outliers = [i for i, *k in outliers]
np.savetxt(outliers_file_name, outliers, delimiter="\n")
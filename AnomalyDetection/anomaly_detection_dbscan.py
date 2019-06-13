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
from sklearn.cluster import DBSCAN
clf = DBSCAN(eps=3, min_samples=5, metric='euclidean')

import time

def parse_timediff(timediff):
    h = timediff // 3600
    m = timediff % 3600 // 60
    s = timediff % 60
    return h, m, s

local_start = time.time()

marks = clf.fit_predict(X)

anomaly_indexes = [i for i, x in enumerate(marks) if x == -1]

hours, minutes, seconds = parse_timediff(time.time() - local_start)

print(hours)
print(minutes)
print(seconds)

neg_lof = np.array(clf.negative_outlier_factor_)
neg_lof.shape
marks = neg_lof.copy()
threshold = 0.01
marks[neg_lof <= np.percentile(neg_lof, threshold)] = -1
marks[neg_lof > np.percentile(neg_lof, threshold)] = 1
outlier_indicates = np.asarray([mark < 0 for mark in marks])

outliers = df[anomaly_indexes]
n_outliers = outliers.shape[0]
n_df = df.shape[0]

import csv

outliers_file_name = file_with_outliers

outliers.to_csv(outliers_file_name, sep='\t', encoding='ISO-8859-1')
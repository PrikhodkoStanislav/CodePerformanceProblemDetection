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
from sklearn import svm

import time

def parse_timediff(timediff):
    h = timediff // 3600
    m = timediff % 3600 // 60
    s = timediff % 60
    return h, m, s

local_start = time.time()

clf = svm.OneClassSVM(kernel="rbf")
clf.fit(X)

hours, minutes, seconds = parse_timediff(time.time() - local_start)

print(hours)
print(minutes)
print(seconds)

dist_to_border = clf.decision_function(X).ravel()
from scipy import stats

outlier_fraction = 0.0001

threshold = stats.scoreatpercentile(dist_to_border, 100 * outlier_fraction)
is_inlier = dist_to_border > threshold
outliers = df[is_inlier == 0]

import csv

outliers_file_name = file_with_outliers

outliers = pd.DataFrame(outliers)

outliers.to_csv(outliers_file_name, sep='\t', encoding='ISO-8859-1')
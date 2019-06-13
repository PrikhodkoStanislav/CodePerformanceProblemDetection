from sklearn.feature_extraction.text import CountVectorizer

vectorizerToken = CountVectorizer(input='filename')
vectors = vectorizerToken.fit_transform(d_values)

print(len(vectors.toarray()))

res_1 = vectors.toarray()

from sklearn.preprocessing import Binarizer

onehot = Binarizer()
corpus = onehot.fit_transform(vectors.toarray())

res_2 = corpus

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf  = TfidfVectorizer(input='filename')
vec_tf_idf = tfidf.fit_transform(d_values)

res_3 = vec_tf_idf.toarray()

feature_names = vectorizerToken.get_feature_names()
res_1_names = ["count_" + feature for feature in feature_names]
res_2_names = ["bin_" + feature for feature in feature_names]
res_3_names = ["tfidf_" + feature for feature in feature_names]

featuresFileName = "features_value_full.tsv"
k = len(d_values)

with open(featuresFileName, 'w') as tsv_file:
    tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
    tsv_writer.writerow(["ID", "Path"] + res_1_names + res_2_names + res_3_names)
    for i in range(0, k):
        tsv_writer.writerow([i + 1] + [d_values[i]] + list(res_1[i]) + list(res_2[i]) + list(res_3[i]))
import os
from collections import defaultdict
from nltk.text import TextCollection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Binarizer

def features():
    f = open("C:/CPPD/Project/file.txt", 'r')
    token_types = [line.split(' (')[0] for line in f]
    print(token_types)
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(token_types)
    #print(vectors)
    vector = vectorize(token_types)
    #print(vector)
    vector = vectorize_bin(token_types)
    #print(vector)
    # freq = CountVectorizer()
    # corpus = freq.fit_transform(token_types)
    # print(corpus)
    # onehot = Binarizer()
    # corpus = onehot.fit_transform(corpus.toarray())
    # print(corpus)
    # tfidf  = TfidfVectorizer()
    # corpus = tfidf.fit_transform(token_types)
    # print(corpus)
    vector = vectorize_t(token_types)
    print(vector)


def vectorize(doc):
    features = defaultdict(int)
    for token in doc:
        features[token] += 1
    return features

def vectorize_bin(doc):
    return {
        token: True
        for token in doc
    }

def vectorize_t(corpus):
    #corpus = [tokenize(doc) for doc in corpus]
    texts = TextCollection(corpus)
    return {
        term: texts.tf_idf(term, corpus)
        for term in corpus
    }

features()
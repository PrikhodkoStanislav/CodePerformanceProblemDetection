
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import scale
from sklearn import svm
from sklearn.decomposition import PCA


# In[4]:


df=pd.read_csv('features.tsv', sep='\t',header=None)

print(df)

print(df.info())

print(df.describe())



# In[6]:


params = np.array(df.values[:,1:], dtype="float64")
params = scale(params)


# In[7]:


X = PCA(n_components=2).fit_transform(params)
num = X.shape[0]
OUTLIER_FRACTION = 0.01


# In[ ]:










# In[8]:


clf = svm.OneClassSVM(kernel="rbf")
clf.fit(X)


# In[9]:


dist_to_border = clf.decision_function(X).ravel()
threshold = stats.scoreatpercentile(dist_to_border,
            100 * OUTLIER_FRACTION)
is_inlier = dist_to_border > threshold


# In[10]:


xx, yy = np.meshgrid(np.linspace(-7, 7, 500), np.linspace(-7, 7, 500))
n_inliers = int((1. - OUTLIER_FRACTION) * num)
n_outliers = int(OUTLIER_FRACTION * num)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Outlier detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                         cmap=plt.cm.Blues_r)
a = plt.contour(xx, yy, Z, levels=[threshold],
                            linewidths=2, colors='red')
plt.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                         colors='orange')
b = plt.scatter(X[is_inlier == 0, 0], X[is_inlier == 0, 1], c='white')
c = plt.scatter(X[is_inlier == 1, 0], X[is_inlier == 1, 1], c='black')
plt.axis('tight')
plt.legend([a.collections[0], b, c],
           ['learned decision function', 'outliers', 'inliers'],
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.xlim((-7, 7))
plt.ylim((-7, 7))
plt.show()


# In[14]:


print(df[is_inlier == 0])


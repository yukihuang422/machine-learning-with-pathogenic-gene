import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from sklearn import decomposition
from sklearn.cluster import AgglomerativeClustering
from sklearn.mixture import GaussianMixture
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import Birch 
sns.set()

matrix =pd.read_csv('fpkm.csv',index_col = 'gene')



ax = plt.figure().add_subplot(111, projection = '3d')

# standardization
matrix =  matrix.apply(lambda x: (x - np.mean(x)) / np.std(x))

# build the heatmap
clustering = AgglomerativeClustering().fit(matrix)
sns_plot = sns.clustermap(matrix.T,method='ward',metric='euclidean')
plt.savefig('./heatmap.png')
plt.show()

matrix_new =  matrix.values

# PCA
pca = decomposition.PCA(n_components=3)
matrix_pca = pca.fit_transform(matrix_new)
# print(pca.explained_variance_ratio_)
# [9.96502724e-01 1.96036416e-03 9.43274914e-04]
ax.scatter(matrix_pca[:, 0], matrix_pca[:, 1], matrix_pca[:, 2], marker='o')
ax.set_xlabel('pca_01')
ax.set_ylabel('pca_02')
ax.set_zlabel('pca_03')
plt.show()

# K-means
kmeans = KMeans(n_clusters=2)
kmeans.fit(matrix_pca)
matrix_kmeans = kmeans.predict(matrix_pca)
for i in range(len(matrix_kmeans)):
    if matrix_kmeans[i] == 0:
        ax.scatter(matrix_pca[i, 0], matrix_pca[i, 1], matrix_pca[i, 2], c = 'b', marker='o')
    else:
        ax.scatter(matrix_pca[i, 0], matrix_pca[i, 1], matrix_pca[i, 2], c = 'r', marker='o')
        print(i)


# DBSCAN  --  计算量过于庞大，且效果不佳

# hierarchical clustering
model = AgglomerativeClustering(n_clusters=2, affinity="euclidean", linkage='average')
labels = model.fit_predict(matrix_new)
for i in range(len(labels)):
    if labels[i] == 1:
        print(i)

# BIRCH
labels = Birch(n_clusters=2).fit_predict(matrix_pca)
for i in range(len(labels)):
    if labels[i] == 1:
        print(i)

# GaussianMixture
gmm = GaussianMixture(n_components=2, covariance_type='full').fit(matrix_pca)
labels = gmm.predict(matrix_pca)
for i in range(len(labels)):
    if labels[i] == 1:
        print(i)





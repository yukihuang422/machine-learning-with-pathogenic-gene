## This python script is used to distinguish three groups of mice and find the pathogenic gene.

## The train dataset file is "fpkm.csv". The file has 10 columns and 16475 rows. The first column is name of different genes. The other 9 columns consists of three groups of mice.

## Since my purpose is to find out which gene is the pathogenic gene, my first step is to build a heatmap with HierarchicalClustering. This plot is saved as "heatmap.png".

## However, the heatmap does not work very well. As a result, I need to use some machine learning methods to find out the pathogenic gene. 

## From the dataset we can see we have 9 columns of gene expressions which means we have nine dimensions in machine learning. Nine dimension space is invisible in reality so my next step is dimension reductioin. The best way to do dimension reduction is PCA. I choose three PCs and their explained variance ratio are [9.96502724e-01 1.96036416e-03 9.43274914e-04].

## After PCA, I make a 3D plot to show all the gene expressions. This plot is saved as "pca.png". From this plot we can clearly know there are some outliers. Of course, the next step is to find out who thses outliers are.

## Because we don't have other labeled train dataset, so we can only choose Unsupervised Learning Methods. I choose K-means, DBSCAN, Hierarchical Clustering, BIRCH and GaussianMixture to do the model training. Among these methods, DBSCAN requires huge computational tasks so this is not a good choice. In the other four methods, I set n_clusters = 2 which means all the genes are divided into two clusters. Cluster with large number of genes is labeled with 0 and another is labeled with 1. Now we have got the idea that the small cluster is the pathogenic gene. 

## The last step is to print all the pathogenic genes. Results are as followed:

## K-means:
## 13339 : ENSRNOG00000034228
## 14887 : ENSRNOG00000046763
## 15103 : ENSRNOG00000047319
## 15335 : ENSRNOG00000047984
## 15423 : ENSRNOG00000048221
## 15559 : ENSRNOG00000048596
## 15676 : ENSRNOG00000048910
## 15713 : ENSRNOG00000048989
## 15779 : ENSRNOG00000049171
## 15825 : ENSRNOG00000049277
## 15945 : ENSRNOG00000049620
## 16450 : ENSRNOG00000050958

## hierarchical clustering
## 15335 : ENSRNOG00000047984

## BIRCH
## 15335 : ENSRNOG00000047984

## GaussianMixture
## 15335 : ENSRNOG00000047984

## Now we have got the result: ENSRNOG00000047984 is the most likely pathogenic gene.
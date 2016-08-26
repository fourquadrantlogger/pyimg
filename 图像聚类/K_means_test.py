# coding:utf-8

from matplotlib.pyplot import plot, show, figure
from numpy.matlib import randn, array, vstack, where
from scipy.cluster.vq import kmeans, vq

# 生成正态分布的二维数据
class1=1.5*randn(100,2)
class2=randn(100,2)+array([5,5])
features=vstack((class1,class2))

# 用k=2对这些数据进行聚类

centroids,variance = kmeans(features,2)

# 通过矢量化函数对每个数据点进行归类:
code,distance=vq(features,centroids)

figure()
ndx=where(code==0)[0]
plot(features[ndx,0],features[ndx,1],'*')
ndx=where(code==1)[0]
plot(features[ndx,0],features[ndx,1],'r.')
plot(features[:,0],features[:,1],'go')
show()


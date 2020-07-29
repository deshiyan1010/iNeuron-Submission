import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data 
y = iris.target

pca = decomposition.PCA(n_components=3)
components = pca.fit_transform(X)

concatenated = np.concatenate((components,y.reshape(-1,1)),axis=1)
colour = {0:'r',1:'b',2:'g'}
label = {0:'Setosa',1:'Versicolor',2:'Virginica'}
ax = plt.axes(projection='3d')
for x,y,z,c in concatenated:  
    ax.scatter(xs=x,ys=y,zs=z,color=colour[c],label=label[c])

handles,labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels,handles))
plt.legend(by_label.values(),by_label.keys())
plt.show()

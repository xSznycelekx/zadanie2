from csv import reader, writer
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import  numpy as np

def readcsv(name,nl="\n",dl=","):
    cloud=[]
    with open(name, newline=nl) as csvfile:
        csvreader=reader(csvfile, delimiter=dl)
        for xx,yy,zz in csvreader:
            cloud.append([float(xx),float(yy),float(zz)])
    return cloud

def writecsv(file_name, cloud_points):
    with open(file_name, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points:
            csvwriter.writerow(p)

cloud=readcsv("lidar_point.xyz")

clusterer = KMeans(n_clusters=3)
X=np.array(cloud)
y_pread=clusterer.fit_predict(X)

red=y_pread==0
blue=y_pread==1
cyan=y_pread==2

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X[red,0],X[red,1],X[red,2],c='r')
ax.scatter(X[blue,0],X[blue,1],X[blue,2],c='b')
ax.scatter(X[cyan,0],X[cyan,1],X[cyan,2],c='c')
plt.show()

r=[]
b=[]
c=[]

for i in range(len(cloud)):
    if red[i]:
        r.append(cloud[1])
    elif blue[i]:
        b.append(cloud[i])
    elif cyan[i]:
        c.append(cloud[i])

writecsv("cloud_r.xyz",r)
writecsv("cloud_b.xyz",b)
writecsv("cloud_c.xyz",c)
from csv import reader
import numpy as np

import pyransac3d as pyran

def readcsv(name, nl="\n",dl=","):
    cloud = []
    with open(name, newline=nl) as csvfile:
        csvreader = reader(csvfile, delimiter=dl)
        for xx, yy, zz in csvreader:
            cloud.append([float(xx), float(yy), float(zz)])
    return cloud


cloud = np.array(readcsv("cloud_r.xyz"))

plane = pyran.Plane()
best_eq, best_inliers = plane.fit(cloud, thresh=0.01, minPoints=100, maxIteration=1000)

print(f'best eq Ax+By+Cz+D:{best_eq}')
print(f'best inliers:{best_inliers}')
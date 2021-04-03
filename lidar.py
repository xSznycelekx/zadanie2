from scipy.stats import norm
from csv import writer
import random as rnd
import numpy as np

def generate_points(num_points, lockx, scalex, locky, scaley, lockz, scalez, push):
    distribution_x = norm(lockx, scalex)
    distribution_y = norm(locky, scaley)
    distribution_z = norm(lockz, scalez)

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x+push, y+push, z+push)
    return points

def generate_cylinder(number_points:int=10000,r=100,h=300,push=0):
    xx=[]
    yy=[]
    zz=[]
    while(len(xx) < number_points):
        x = rnd.uniform(-1,1)*r
        y = rnd.uniform(-1,1)*np.sqrt(r**2-x**2)
        z = rnd.uniform(-1,1)*h

        xx.append(x+push)
        yy.append(y+push)
        zz.append(z+push)

    return zip(xx,yy,zz)

if __name__=='__main__':
    cloud1_points=generate_points(1000,0,100,0,100,0,1,500)
    cloud2_points=generate_points(1000,0,1,0,100,0,100,-500)
    cylinder_points=generate_cylinder(1000)
    with open('lidar_point.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter=writer(csvfile)
        for p1 in cloud1_points:
            csvwriter.writerow(p1)
        for p2 in cloud2_points:
            csvwriter.writerow(p2)
        for p3 in cylinder_points:
            csvwriter.writerow(p3)
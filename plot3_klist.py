#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import argparse
from mpl_toolkits import mplot3d

desc = """
    plot klist

"""
parser = argparse.ArgumentParser(  description = desc  )
parser.add_argument('f',type=str,help='klist file')
parser.add_argument('-l',type=int,default=None,help='the former l line')

p = parser.parse_args()
fn = open(p.f)
kls = fn.readlines()

kl = np.zeros([len(kls),5])
for n in range(len(kls)):
    #print kls[n].split()
    if kls[n][0:3]=='END' or kls[n].split()=='': break
    kl[n,:] = list(map(int, kls[n].split()[0:5]))

kl = kl[0:n]
for n in range(n):
    kl[n,1:4] = kl[n,1:4]/kl[n,4]

if p.l is not None: kl = kl[0:p.l]

ax = plt.axes(projection='3d')
ax.plot3D(kl[:,1],kl[:,2],kl[:,3],'-o')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

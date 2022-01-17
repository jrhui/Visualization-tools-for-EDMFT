#!/usr/bin/env python
import matplotlib.pyplot as plt
import argparse
import csv 
import numpy as np
desc = """
plot data from a csv-like file with multi-y columns, \n
e.g. plot.py data.dat -y 2 4 \n

(if yi<0, then -data[:,-yi] will be plotted)
"""

parser = argparse.ArgumentParser(  description = desc  )
parser.add_argument('str',type=str,help='file name')
parser.add_argument('-x',nargs=1,default=0,type=int,help='x-axis, if x=-1, we will use 0,1,2,3... as the x-axis, default: 0')
parser.add_argument('-y',nargs='+',required=True,type=int,help='y-axis')
parser.add_argument('-xl',nargs=2,default=None,type=float,help='xlim')
parser.add_argument('-yl',nargs=2,default=None,type=float,help='ylim')
parser.add_argument('-kw',nargs=1,type=dict,help='kwargs')
parser.add_argument('-xlb',nargs=1,default=None,type=str,help='xlabel')
parser.add_argument('-ylb',nargs=1,default=None,type=str,help='ylabel')
parser.add_argument('-leg',nargs='+',default=None,type=str,help='legend')
parser.add_argument('-tit',nargs=1,default=None,type=str,help='tit')
parser.add_argument('-s',nargs=1,default=False,type=bool,help='save as fig.png? default: 0')
parser.add_argument('-l',nargs=1,default=None,type=int,help='only plot last l lines')
parser.add_argument('-c',nargs='+',default=None,type=int,help='use c1 c2...   column')


p = parser.parse_args()
if isinstance(p.x,list): xi = p.x[0]
else: xi = p.x
yi = p.y
#print(p.c)
data = np.loadtxt(p.str,usecols=p.c)

if p.l is not None: data = data[-p.l[0]:]

for i in range(len(yi)):
    if yi[i]<0:
        yi[i] = -yi[i]
        data[:,yi[i]] = -data[:,yi[i]]

#print(yi)
if xi==-1: xax = np.arange(len(data))
else: xax = data[:,xi]

plt.plot(xax, data[:,yi],'-o',markersize=2)
#plt.plot(data[:,xi], data[:,yi[0]],'-')
#plt.plot(data[:,xi], data[:,yi[1]]*2,'-')
plt.xlim(p.xl)
plt.ylim(p.yl)
if p.xlb is not None: plt.xlabel('$'+p.xlb[0]+'$')
if p.ylb is not None: plt.ylabel('$'+p.ylb[0]+'$')
if p.leg is not None: plt.legend(['$'+_+'$' for _ in p.leg])
if p.tit is not None: plt.title('$'+p.tit[0]+'$')
if p.s: plt.savefig('fig.png')
plt.show()


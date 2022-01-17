#!/usr/bin/env python

import numpy as np
from Suscept import ReadVertex
import argparse
import matplotlib.pyplot as plt

desc = """
    plot tertex.dat for visualization.
"""
parser = argparse.ArgumentParser(  description = desc  )
parser.add_argument('-x',nargs=3,type=str,help='x-axis')
parser.add_argument('-hf',nargs=1,type=str,default=['hf'],help='h, f or hf?')
parser.add_argument('-ri',nargs=1,type=str,default=['ri'],help='r(eal), i(magine) or ri? default: ri')
parser.add_argument('-o',nargs='+',type=int,default=[0,0],help='orbital, default: 0 0')
parser.add_argument('-f',nargs=1,type=str,default=['tvertex.dat'],help='vertex file, default: tvertex.dat')

p = parser.parse_args()

beta,Nvfl,nomv,nOm,bfl_index,VertexH,VertexF = ReadVertex(p.f[0])
print 'beta=', beta, ' Nvfl=', Nvfl, 'nOm=', nOm, 'nomv=', nomv, 'bfl_index=', bfl_index
        
if p.x[0]==':':
    x1 = int(p.x[1])+nomv; x2 = int(p.x[2])+nomv
    VH = VertexH[...,:,x1,x2]; VF = VertexF[...,:,x1,x2]
    xa = np.arange(-nOm+1,nOm); xal = '$\omega_n$'
elif p.x[1]==':':
    x1 = int(p.x[0])+nOm-1; x2 = int(p.x[2])+nomv
    VH = VertexH[...,x1,:,x2]; VF = VertexF[...,x1,:,x2]
    xa = np.arange(-nomv,nomv); xal = '$\nu_n$'
elif p.x[2]==':':
    x1 = int(p.x[0])+nOm-1; x2 = int(p.x[1])+nomv
    VH = VertexH[...,x1,x2,:]; VF = VertexF[...,x1,x2,:]
    xa = np.arange(-nomv,nomv); xal = '$\nu_n$'
else:
    print('error in -x')

for no in range(len(p.o)//2):
    o1 = p.o[no*2]; o2 = p.o[no*2+1]
    if 'h' in p.hf[0]:
        if 'r' in p.ri[0]:
            plt.plot(xa, VH[o1,o2].real,'-o',c='C%d'%no,label='ReV_H '+str(o1)+' '+str(o2))
        if 'i' in p.ri[0]:
            plt.plot(xa, VH[o1,o2].imag,'-^',c='C%d'%no,label='ImV_H '+str(o1)+' '+str(o2))
    if 'f' in p.hf[0]:
        if 'r' in p.ri[0]:
            plt.plot(xa, VF[o1,o2].real,'-s',c='C%d'%no,label='ReV_F '+str(o1)+' '+str(o2))
        if 'i' in p.ri[0]:
            plt.plot(xa, VF[o1,o2].imag,'-<',c='C%d'%no,label='ImV_F '+str(o1)+' '+str(o2))

plt.xlabel(xal)
plt.legend()
plt.show()

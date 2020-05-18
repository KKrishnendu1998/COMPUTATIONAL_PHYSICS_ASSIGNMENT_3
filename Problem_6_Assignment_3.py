#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 6 : Python code to compute Fourieform of a constant function

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x):            #defining a constant function
    return 2
    
xmin=-10
xmax=10

numpoints=32                   #number of points

dx=(xmax-xmin)/(numpoints-1)     

sampled_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)

for i in range(numpoints):
    sampled_data[i]=fun(xmin+i*dx)           #sampling the data
    xarr[i]=xmin+i*dx
    


karr=np.zeros(numpoints)
n=np.arange(-numpoints/2,numpoints/2,1)
for i in range(numpoints):                          #computing the frequecies
    karr[i]=2*np.pi*n[i]/(numpoints*dx)    
    
f=np.zeros(numpoints,dtype="complex")

for i in range(numpoints):
    for k in range(numpoints):                           #computing the Fourier transform
        
        f[i]+=sampled_data[k]*np.exp(-1j*karr[i]*xarr[k]) /np.sqrt(2*np.pi) 
        
plt.plot(karr,abs(f))
plt.xlabel("frequencies(k)")
plt.show()
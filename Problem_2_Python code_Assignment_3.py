#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 2:Python code to plot the Fourier transform of the sinc function obtained from the C code

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(k):       #defining the function for the analytical Fourier transform
    return 0.5*np.sqrt(np.pi/2)*(np.sign(k+1)-np.sign(k-1))

k=np.loadtxt("Problem2.txt",usecols=[0],dtype="float")
y1=np.loadtxt("Problem2.txt",usecols=[1],dtype="float")
y2=np.loadtxt("Problem2.txt",usecols=[2],dtype="float")
y=abs(np.sqrt(y1**2+y2**2))

m=k.argsort()
y=y[m]
k=np.sort(k)

plt.plot(k,y,label="using FFTW")
plt.plot(k,fun(k),label="Analytical")
plt.legend()
plt.xlabel("frequencies(k)")
plt.show()

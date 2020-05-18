#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 3: Python code to plot the fourier transform of the sinc function obtained from the c code using GSL

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(k):       #defining the function for the analytical Fourier transform
    return 0.5*np.sqrt(np.pi/2)*(np.sign(k+1)-np.sign(k-1))

k=np.loadtxt("Problem3.txt",usecols=[2],dtype="float")
y1=np.loadtxt("Problem3.txt",usecols=[3],dtype="float")
k=np.fft.fftshift(k)

y1=np.fft.fftshift(y1)

plt.plot(k,y1,label="using FFTW")
plt.plot(k,fun(k),label="Analytical")
plt.legend()
plt.xlabel("frequencies(k)")
plt.show()

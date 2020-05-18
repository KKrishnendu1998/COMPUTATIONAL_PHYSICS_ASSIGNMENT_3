#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 9 : Python code to compute the convolution of the box function with itself.

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import *

def fun(x):     #defining the box function
    if(x>-1 and x<1):
        return 1
    else :
       return  0
    
xmin=-5
xmax=5

numpoints=1023

dx=(xmax-xmin)/(numpoints-1)
n=2*numpoints+1
sampled_data=np.zeros(n)



for i in range(numpoints):
    sampled_data[i]=fun(xmin+i*dx)
    
nft=np.fft.fft(sampled_data,norm='ortho')    #doing DFT of the function

nft=nft*nft

fx=np.fft.ifft(nft,norm="ortho")

fx=dx*np.sqrt(n)*fx


plt.plot(np.linspace(xmin,xmax,numpoints),fx[int(numpoints/2):int(3*numpoints/2)],label="Convolution")

plt.plot(np.linspace(xmin,xmax,numpoints),sampled_data[0:numpoints],label="Box function")
plt.legend()
plt.xlabel("x")
plt.grid()
plt.show()
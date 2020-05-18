#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem1 : Python code to compute the Fourier transform of the sinc function

@author: krishnendu
"""
import numpy as np
import matplotlib.pyplot as plt

def fun(x):            #defining the sinc function
    if(x==0):
        return 1
    else :
     return np.sin(x)/x


def fun1(k):
    return 0.5*np.sqrt(np.pi/2)*(np.sign(k+1)-np.sign(k-1))
   
       
    
xmin=-500              #xmin value
xmax=500             #xmax value

numpoints=1024         #number of sample points

dx=(xmax-xmin)/(numpoints-1)      

sampled_data=np.zeros(numpoints)

xarr=np.zeros(numpoints)

for i in range(numpoints):
    sampled_data[i]=fun(xmin+i*dx)          #sampling the data
    xarr[i]=xmin+i*dx

nft=np.fft.fft(sampled_data,norm='ortho')       #computing dft of the data using numpy.fft.fft

karr=np.fft.fftfreq(numpoints,d=dx)          #computing the frequencies 

karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)
aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft
karr=np.fft.fftshift(karr)         #shifting the frequencies

aft=np.fft.fftshift(aft)           #shifting the fourier transform

plt.plot(karr,abs(aft))       #plotting the fourier transform computed by numpy.fft.fft
plt.plot(karr,fun1(karr))    #plotting the fourier transform obtained analytically
plt.xlim(-3,3)
plt.xlabel("frequency(k)")
plt.show()
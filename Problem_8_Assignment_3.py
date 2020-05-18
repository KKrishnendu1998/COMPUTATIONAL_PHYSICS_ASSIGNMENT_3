#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 8: Python code for computing two-dimensional Fourier transform of the Gaussian function using numpy.fft.fft2


@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def fun(x,y):     #defining the function
    return np.exp(-(x**2+y**2))

def fun1(kx,ky):
     X,Y=np.meshgrid(kx,ky)
     return np.exp(-(X**2+Y**2)/4)/2**1.5
xmin=-50
xmax=50
ymin=-50
ymax=50

numpoints=512    #number of sampling points

dx=(xmax-xmin)/(numpoints-1)
dy=dx
xarr=np.linspace(xmin,xmax,numpoints)   #creating the x array
    
yarr=np.copy(xarr)           #taking the y array same as the y array

karrX=np.fft.fftfreq(numpoints,d=dx)   #computing the frequencies corresponding to the x axis

karrY=np.fft.fftfreq(numpoints,d=dy)   #computing the frequencies corresponding to the y axis


X,Y=np.meshgrid(xarr,yarr)

f=fun(X,Y)              #sampling the function

nft=np.fft.fft2(f,norm='ortho')     #computing the DFT of the function

karrX=2*np.pi*karrX      #computing the frequencies corresponding to the x array

karrY=2*np.pi*karrY     #computing the frequencies corresponding to the y array
 

factorX=np.exp(-1j*karrX*xmin)
factorY=np.exp(-1j*karrY*ymin)

Z=dx*dy*(numpoints/(2.0*np.pi))*factorX*factorY*nft       #computing the fft of the function
Z=np.fft.fftshift(Z)
karrX=np.fft.fftshift(karrX)

karrY=np.fft.fftshift(karrY)

KX,KY=np.meshgrid(karrX,karrY)

fig=plt.figure(figsize=plt.figaspect(0.4))
ax1=fig.add_subplot(1,2,1,projection='3d')

ax1.contour3D(karrX,karrY,abs(Z),100)             #plotting the FFT of the function computed using numpy.fft.fft2
ax1.set_title("using numpy.fft.fft2")
ax1.set_xlabel("kx")
ax1.set_ylabel("ky")

ax1=fig.add_subplot(1,2,2,projection='3d')


ax1.contour3D(karrX,karrY,fun1(karrX,karrY),100)        #plotting the FFT of the function computed using numpy.fft.fft2

ax1.set_title("analytical")
ax1.set_xlabel("kx")
ax1.set_ylabel("ky")


plt.show()
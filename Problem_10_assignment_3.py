#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10: Compute the power spectrum of a given data using periodogram

@author: krishnendu
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
y=np.loadtxt("ass3",usecols=0)   #importing the data 

n=len(y)
x=np.arange(1,n+1,1)

plt.plot(x,y)
plt.title("measurement")
plt.xlabel("x")

plt.show()



k=np.fft.fftfreq(n,1)
k=np.fft.fftshift(k)
dft=np.fft.fft(y)
dft=np.fft.fftshift(dft)

plt.plot(k,dft)
plt.title("dft of the data")
plt.xlabel("frequencies(k)")
plt.show()


"""Method 1: """


pdg1=abs(dft)**2/n
plt.plot(k,pdg1)
plt.title("periodogram")
plt.xlabel("frequencies(k)")
plt.show()

#By binned data 
y0=y[0:510].reshape(10,51)

k0=np.fft.fftfreq(51,1)
k0=np.fft.fftshift(k0)

pdg2=np.zeros(510).reshape(10,51)


for i in range(10):
    z=np.fft.fft(y0[i])
    z=np.fft.fftshift(z)
    pdg2[i]=(abs(z)**2)/51
    
pdg2=sum(pdg2[:,])/10

plt.plot(k0,pdg2) 
plt.title("periodogram using binned data" )   
plt.xlabel("frequencies(k)") 
plt.show()



"""Method 2: By computing the correlation function of the data"""
f=np.zeros(n)

for i in range(n):         #computing the correlation of the data
    
        f[i]=sum(y[:n-i]*y[i:])/n
 
    
fk=np.fft.fft(f)          #doing the dft of the correlation function

fk=np.fft.fftshift(fk)
                          #computing the frequencies considering the sampling frequency=1






plt.plot(k,abs(fk))
plt.xlabel("frequencies(k)")
plt.title("using FFT of correlation function")

plt.show()
  
fs=1     #sampling frequency
fp,pxx_den=signal.periodogram(y,fs,scaling="spectrum",return_onesided=False ) 
fp=np.fft.fftshift(fp)
pxx_den=np.fft.fftshift(pxx_den)  

plt.plot(fp,abs(pxx_den))
plt.title("using scipy.signal.periodogram")
plt.xlabel("frequencies(k)")
plt.show()


"""Binned power spectrum """

y1=y[0:510].reshape(10,51)

f2=np.zeros(510).reshape(10,51)
fk2=np.zeros(510).reshape(10,51)

for k in range(10):
    for i in range(51):
         f2[k][i]=sum(y1[k][:51-i]*y1[k][i:])/51
         
    fk2[k]=np.fft.fft(f2[k])
    fk2[k]=np.fft.fftshift(fk2[k])   
    
fk2=sum(fk2[:,])/10

k2=np.fft.fftfreq(51,1)
k2=np.fft.fftshift(k2)



plt.plot(k2,abs(fk2))
plt.title("binned power spectrum using correlation function")
plt.xlabel("frequencies(k)")
plt.show()
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




f=np.zeros(n)

for i in range(n):         #computing the correlation of the data
    
        f[i]=sum(y[:n-i]*y[i:])/n
 
    
fk=np.fft.fft(f)          #doing the dft of the correlation function

fk=np.fft.fftshift(fk)

k=np.fft.fftfreq(n,1)    #computing the frequencies considering the sampling frequency=1

k=np.fft.fftshift(k)




plt.plot(k,abs(fk))
plt.xlabel("frequency(k)")
plt.title("using FFT of correlation function")

plt.show()
  
fs=1     #sampling frequency
fp,pxx_den=signal.periodogram(y,fs,scaling="spectrum",return_onesided=False )   

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
plt.title("binned power spectrum")
plt.xlabel("frequencies(k)")
plt.show()
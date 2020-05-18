#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROBLEM 5: Take n numbers and write a Python code to compute their DFT using direct computation i.e, without using
FFT.The compute the same DFT using numpy.fft.fft. Measure the time taken by the two methods.Now change the number 
n over a wide range of values ,say from 4 to 100,and repeat the exercise.Make a plot showing the time taken by the 
two DFT methods as a function of n.


@author: krishnendu
"""

import numpy as np
import time
import matplotlib.pyplot as plt

"""Computing the DFT of n numbers given by the user by direct computation and then by using numpy.fft.fft and measure the 
the time for both the cases"""


n=int(input("Enter the length off the array :"))        #input from the user  

a=np.empty(n)
for i in range(n):                                      #input from the user
    ele=float(input("Enter the next elements:"))
    a[i]=ele
    
f=np.zeros(n,dtype="complex")

start_time1=time.time()               #initializing the time for direct computation

for i in range(n):                    #computing the DFT by direct computation
    for k in range(n):
        f[i]+=a[k]*np.exp(-2j*np.pi*i*k/n)/np.sqrt(n)
        
stop_time1=time.time()                #stopping the time for direct computation 
   
print(f)                             #printing the value of DFT obtained by direct computation

print("the time required by using code :",stop_time1-start_time1)  #printing the time required to compute DFT using direct computation

start_time2=time.time()       #initializing time for computing DFT using numpy.fft.fft

f2=np.fft.fft(a,norm="ortho")          #computing DFT using numpy.fft.fft

stop_time2=time.time()               #stopping the time for computing using numpy.fft.fft

print(f2)                         #printing the DFT computed using numpy.fft.fft

print("the time required by using numpy.fft:",stop_time2-start_time2)              #printing the time required to compute DFT using numpy.fft.fft

"""Computing the DFT for a wide range of values of n(from 4 to 100). For n numbers we take the array as [1,2,3,...,n]"""


time1=[]
time2=[]

for i in range(4,101):     #iteration                     
    
    a=np.arange(1,i+1,1)           #constructing the arrray
    
    f=np.zeros(i,dtype="complex")
    
    start_time1=time.time()       #starting the time for computing DFT using direct computation
    
    for q in range(i):            #computing the DFT using direct computation
        for p in range(i):
            f[q]+=a[p]*np.exp(-2j*np.pi*p*q/i)/np.sqrt(i)
    
    stop_time1=time.time()        #stopping the time for computing DFT using direct computation
    
    time1.append(stop_time1-start_time1)     #calculating the time taken  for computing DFT using direct computation
    
    start_time2=time.time()        #starting the time for computing DFT using   numpy.fft.fft     
    
    f2=np.fft.fft(a,norm="ortho")     #computing DFT using numpy.fft.fft
    
    stop_time2=time.time()            #stopping time for computing DFT using numpy.fft.fft
    
    time2.append(stop_time2-start_time2) 

plt.plot(np.arange(4,101,1),time1,label="using code")    #plotting time required for computing DFT using direct computation

plt.plot(np.arange(4,101,1),time2,label="using np.fft")   #plotting time required for computing DFT using numpy.fft.fft
plt.xlabel("n")
plt.ylabel("time")
plt.legend()
plt.show()
print(time2)


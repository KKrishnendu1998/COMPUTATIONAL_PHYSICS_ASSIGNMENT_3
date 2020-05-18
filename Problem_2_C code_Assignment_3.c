/*C Code to compute Fourier transform of the sinc function

Note : In this code I have printed the ouput in a file .Then plotted the result using python code

Author : Krishnendu Maji
*/
#include<stdio.h>
#include<stdlib.h>
#include<fftw3.h>
#include<math.h>
#include<complex.h>
float fun(float x)      //defining the sinc function
{
if(x==0){
return 1;
}
else
{
return sin(x)/x;
}
}
void main()
{
int xmin,xmax,numpoints,i,j,k,m;        //declaring variables
double complex z1,z2,z;                 //declaring variables
FILE *data;

data=fopen("ass3_2.txt","w");         //creating a file

xmin=-50;
xmax=50;
numpoints=512;
float xarr[numpoints],dx,karr[numpoints],pi;    //declaring variables

pi=4*atan(1);

dx=(float)(xmax-xmin)/(numpoints-1);


for(i=0;i<numpoints;i++)
{
xarr[i]=xmin+i*dx;
}

for(i=0;i<numpoints;i++)                 //computing the frequencies
{
if(i<numpoints/2)
{

karr[i]=2*pi*i/(numpoints*dx);

}
else
{
karr[i]=2*pi*(i-numpoints)/(numpoints*dx);

}
}

fftw_complex w_p[numpoints],tw_q[numpoints];               
fftw_plan p;
for(j=0;j<numpoints;j++)     //sampling the data
{
w_p[j][0]=fun(xarr[j]);
w_p[j][1]=0;
}

p=fftw_plan_dft_1d(numpoints,w_p,tw_q,FFTW_FORWARD,FFTW_ESTIMATE);     //computing the DFT

fftw_execute(p);
for(m=0;m<numpoints;m++)
{
z1=cos(2*pi*xmin*karr[m])-sin(2*pi*xmin*karr[m])*I;
z2=tw_q[m][0]+tw_q[m][1]*I;

z=dx*z1*z2/sqrt(2*pi);          // Computing the FFT

fprintf(data,"%f  %e  %e\n",karr[m],creal(z),cimag(z));     //printing the output in the file 
}

fclose(data);
fftw_destroy_plan(p);
}	

/*
Problem 3:C code to compute the fourier transform of a sinc function using GSL

Note : In this code I have printed the ouput in a file .Then plotted the result using python code

Author : Krishnendu Maji
*/




#include <stdio.h>
#include<stdlib.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])

double f(double x)
{
  if(x == 0.0)
    {
     return 1.0;}
  else
    {
     return (sin(x)/x);}
}


int main()
{
  int n = 1024;   
  double xmin = -50.0;
  double xmax = 50.0;
  double xarr[n],karr[n],fact_q[2*n],f_data[n],ft_f_data[2*n],pi;
  int i;
  double p[2*n];
  FILE *ft_data;
  double d = (xmax-xmin)/(n-1);
  ft_data = fopen("gsl.txt","w");
  pi=4*atan(1);

  for ( i = 0; i < n; i++)
    {
      xarr[i] = xmin + i*d;
      if(i<n/2)
        karr[i] = 2*pi*(i/(n*d));
      else
        karr[i] = 2*pi*((i-n)/(n*d));
      f_data[i] = f(xarr[i]);

      REAL(ft_f_data,i) = f(xarr[i]); 

      IMAG(ft_f_data,i) = 0.0;
      REAL(fact_q,i) = cos(karr[i]*xmin) ;
      IMAG(fact_q,i) = -sin(karr[i]*xmin);
    }

  gsl_fft_complex_radix2_transform(ft_f_data, 1, n,+1);


for(i = 0;i<n;i++)
{
  
  REAL(ft_f_data,i) = (1.0/sqrt(n))*REAL(ft_f_data,i);
  IMAG(ft_f_data,i) = (1.0/sqrt(n))*IMAG(ft_f_data,i);
 
}

  for(int i = 0;i<n;i++)
  {
    REAL(p,i) = REAL(fact_q,i)*REAL(ft_f_data,i) - IMAG(fact_q,i)*IMAG(ft_f_data,i);
    IMAG(p,i) = REAL(fact_q,i)*IMAG(ft_f_data,i) + IMAG(fact_q,i)*REAL(ft_f_data,i);
   
  }
  

for(i = 0;i<n;i++)
{
  REAL(p,i) = d*sqrt(n/(2*pi))*REAL(p,i);
  printf("%d %f %f\n", i,karr[i],REAL(p,i));
} 

for(i = 0;i<n;i++)
{
 
   
  fprintf(ft_data,"%f  %f  %f  %f\n",xarr[i],f_data[i],karr[i],REAL(p,i));
} 
fclose(ft_data);
  return 0;
}

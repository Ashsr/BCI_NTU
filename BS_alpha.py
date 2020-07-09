import numpy
import pyeeg
import pygame
from scipy.signal import*
from scipy import*
import csv
import scipy.io
mat = scipy.io.loadmat('n1.mat')
bn= mat['Num1']
print shape(bn)
#print bn
bn=bn[0,:]
print shape(bn)
#print bn
p=[]
s=0
a=[]
av = list(csv.reader(open('Baseline.csv')))   
data = list(csv.reader(open('EEG_Data.csv')))
ch = [0,30]
y=numpy.zeros((len(data)-4,2))
for j in range(0,len(ch)):
 for i in range(4,len(data)):
     
   y[i-4][j]=float(data[i][ch[j]])-float(av[1][j])
print shape(y)   
for j in range(0,2):
    a=[]
    for i in range(0,len(data)-4):
        a.append(y[i][j])
    p=convolve(bn,a)
    p=p[:len(data)-4]
    p=p*p
    p=numpy.mean(p)
    print p
    s=s+p
    print s
s=s/2
print s
with open('Alpha_power_baseline.csv','ab') as f:

         cx=csv.writer(f)
         cx.writerow([s])



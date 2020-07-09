import numpy
import pyeeg
import pygame
from scipy.signal import*
from scipy import*
import csv
import scipy.io
mat = scipy.io.loadmat('n2.mat')
bn= mat['num']
print shape(bn)
print bn
bn=bn[0,:]
print shape(bn)
#print bn
p=[]
c=[]
a=[]
av = list(csv.reader(open('Baseline_b.csv')))   
data = list(csv.reader(open('EEG_Data.csv')))
ch = [7,23]
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
    c.append(p)
    print c
with open('SMR_power_baseline.csv','ab') as f:

         cx=csv.writer(f)
         cx.writerow(c)


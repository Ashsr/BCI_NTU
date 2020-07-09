import csv
import numpy


av=[]

data = list(csv.reader(open('EEG_Data.csv')))
ch = [0,30]
y=numpy.zeros((len(data)-4,2))
for j in range(0,len(ch)):
 for i in range(4,len(data)-1):
  y[i-4][j]=data[i][ch[j]]
 
av=numpy.mean(y,axis=0)

with open('Baseline.csv','wb') as f:

         cx=csv.writer(f)
         cx.writerow('Baseline')
         cx.writerow(av) 
print av

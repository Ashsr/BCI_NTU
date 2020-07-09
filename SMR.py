import pygame
from pygame.locals import *
import ctypes
import csv
import Baseline_b
import BSSMR
from scipy.signal import*
from scipy import*
import numpy as np
import scipy.io
mat = scipy.io.loadmat('n2.mat')
bn= mat['num']
bn=bn[0,:]
p=[]
a=[]
with open('SMR_power_left.csv','wb') as f:
         cx=csv.writer(f)
         cx.writerow([])
with open('SMR_power_right.csv','wb') as f:
         cx=csv.writer(f)
         cx.writerow([])
clock=pygame.time.Clock()
Red=(225,0,0)
White=(255,255,255)
BLUE=(0,0,255)
Green=(0,255,0)
Black=(0,0,0)

ir=5
pygame.init()
DISPLAYSURF=pygame.display.set_mode((1300,700),pygame.FULLSCREEN)
DISPLAYSURF.fill(Black)
balImg=pygame.image.load('ball.jpg')
cross=pygame.image.load('cross.png')
right=pygame.image.load('right.png')
left=pygame.image.load('left.png')
crossy=100
crossx=250
arrowx=500
arrowy=500
balx=555
baly=200
while True:
    milli1=0
    DISPLAYSURF.fill(Black)
    DISPLAYSURF.blit(balImg,(balx,baly))
    while(ir!=0):
     with open('EEG_Data.csv','ab') as f:
         cx=csv.writer(f)
         cx.writerow('Right')
         cx.writerow([]) 
     DISPLAYSURF.fill(Black)
     DISPLAYSURF.blit(balImg,(balx,baly))   
     milli1+=clock.tick_busy_loop()
     pygame.display.update()
     while(milli1>5000)&(milli1<6000):
         DISPLAYSURF.blit(cross,(crossx,crossy))
         DISPLAYSURF.blit(balImg,(balx,baly))
         milli1+=clock.tick_busy_loop()
         pygame.display.update()
     while(milli1>6000)&(milli1<8000):
      DISPLAYSURF.blit(right,(arrowx,arrowy))
      DISPLAYSURF.blit(cross,(crossx,crossy))
      milli1+=clock.tick_busy_loop()
      DISPLAYSURF.blit(balImg,(balx,baly))
      pygame.display.update()
      print milli1
      import scipy.io
      mat = scipy.io.loadmat('n2.mat')
      bn= mat['num']
      bn=bn[0,:]
      p=[]
      c=[]
      a=[]
      pygame.time.wait(1000)
      av = list(csv.reader(open('Baseline_b.csv')))   
      data = list(csv.reader(open('Data.csv')))
      blap = list(csv.reader(open('SMR_power_baseline.csv')))
      ch = [7,23]
      y=np.zeros((len(data)-1,2))
      for j in range(0,len(ch)):
       for i in range(0,len(data)-1):
         y[i][j]=float(data[i][ch[j]])-float(av[1][j])
      for j in range(0,2):
       a=[] 
       for i in range(0,len(data)-1):
        a.append(y[i][j])
       p=convolve(bn,a)
       p=p[:500]
       p=p*p
       p=np.mean(p)         
       c.append(p)
      blap=np.asarray(blap)
      print blap
      for i in range(0,2):
       c[i]=c[i]/float(blap[0][i])
       print float(blap[0][i])
      print c
      with open('SMR_power_right.csv','ab') as f:
 
         cx=csv.writer(f)
         cx.writerow(c)
      if (c[0]<c[1]):
          balx=balx+100*int(c[1]-c[0])
          if balx>1200:
              balx=1250
      
     while(milli1>8000)&(milli1<10000):
      DISPLAYSURF.blit(cross,(crossx,crossy))
      DISPLAYSURF.blit(balImg,(balx,baly))
      milli1+=clock.tick_busy_loop()
      pygame.display.update()
      print milli1
      import scipy.io
      mat = scipy.io.loadmat('n2.mat')
      bn= mat['num']
      bn=bn[0,:]
      p=[]
      c=[]
      a=[]
      pygame.time.wait(1000)
      av = list(csv.reader(open('Baseline_b.csv')))   
      data = list(csv.reader(open('Data.csv')))
      blap = list(csv.reader(open('SMR_power_baseline.csv')))
      ch = [7,23]
      y=np.zeros((len(data)-1,2))
      for j in range(0,len(ch)):
       for i in range(0,len(data)-1):
         y[i][j]=float(data[i][ch[j]])-float(av[1][j])
      for j in range(0,2):
       a=[] 
       for i in range(0,len(data)-1):
        a.append(y[i][j])
       p=convolve(bn,a)
       p=p[:500]
       p=p*p
       p=np.mean(p)         
       c.append(p)
      blap=np.asarray(blap)
      print blap
      for i in range(0,2):
       c[i]=c[i]/float(blap[0][i])
       print float(blap[0][i])
      print c
      with open('SMR_power_right.csv','ab') as f:
 
         cx=csv.writer(f)
         cx.writerow(c)
      if (c[0]<c[1]):
          balx=balx+100*int(c[1]-c[0])
          if balx>1200:
              balx=1250
     while(milli1>10000):
        balx=555
        DISPLAYSURF.blit(balImg,(balx,baly)) 
        milli1+=clock.tick_busy_loop() 
        if(milli1>11000):
         milli1=0
         ir=ir-1
         break
    
    ir=5
    while (ir!=0):
     DISPLAYSURF.fill(Black)
     DISPLAYSURF.blit(balImg,(balx,baly))
     with open('EEG_Data.csv','ab') as f:
         cx=csv.writer(f)
         cx.writerow('Left')
         cx.writerow([])   
     DISPLAYSURF.fill(Black)
     DISPLAYSURF.blit(balImg,(balx,baly))   
     milli1+=clock.tick_busy_loop()
     pygame.display.update()
     while(milli1>5000)&(milli1<6000):
         DISPLAYSURF.blit(cross,(crossx,crossy))
         DISPLAYSURF.blit(balImg,(balx,baly))
         milli1+=clock.tick_busy_loop()
         pygame.display.update()
     while(milli1>6000)&(milli1<8000):
      DISPLAYSURF.blit(left,(arrowx,arrowy))
      DISPLAYSURF.blit(cross,(crossx,crossy))
      DISPLAYSURF.blit(balImg,(balx,baly))
      milli1+=clock.tick_busy_loop()
      pygame.display.update()
      print milli1
      import scipy.io
      mat = scipy.io.loadmat('n2.mat')
      bn= mat['num']
      bn=bn[0,:]
      p=[]
      c=[]
      a=[]
      pygame.time.wait(1000)
      av = list(csv.reader(open('Baseline_b.csv')))   
      data = list(csv.reader(open('Data.csv')))
      blap = list(csv.reader(open('SMR_power_baseline.csv')))
      ch = [7,23]
      y=np.zeros((len(data)-1,2))
      for j in range(0,len(ch)):
       for i in range(0,len(data)-1):
         y[i][j]=float(data[i][ch[j]])-float(av[1][j])
      for j in range(0,2):
       a=[] 
       for i in range(0,len(data)-1):
        a.append(y[i][j])
       p=convolve(bn,a)
       p=p[:500]
       p=p*p
       p=np.mean(p)         
       c.append(p)
      blap=np.asarray(blap)
      print blap
      for i in range(0,2):
       c[i]=c[i]/float(blap[0][i])
       print float(blap[0][i])
      print c
      with open('SMR_power_left.csv','ab') as f:
 
         cx=csv.writer(f)
         cx.writerow(c)
      if (c[0]>c[1]):
          balx=balx+100*int(c[1]-c[0])
          if balx<10:
              balx=10
      
     while(milli1>8000)&(milli1<10000):
      DISPLAYSURF.blit(cross,(crossx,crossy))
      DISPLAYSURF.blit(balImg,(balx,baly))
      milli1+=clock.tick_busy_loop()
      pygame.display.update()
      print milli1
      import scipy.io
      mat = scipy.io.loadmat('n2.mat')
      bn= mat['num']
      bn=bn[0,:]
      p=[]
      c=[]
      a=[]
      pygame.time.wait(1000)
      av = list(csv.reader(open('Baseline_b.csv')))   
      data = list(csv.reader(open('Data.csv')))
      blap = list(csv.reader(open('SMR_power_baseline.csv')))
      ch = [7,23]
      y=np.zeros((len(data)-1,2))
      for j in range(0,len(ch)):
       for i in range(0,len(data)-1):
         y[i][j]=float(data[i][ch[j]])-float(av[1][j])
      for j in range(0,2):
       a=[] 
       for i in range(0,len(data)-1):
        a.append(y[i][j])
       p=convolve(bn,a)
       p=p[:500]
       p=p*p
       p=np.mean(p)         
       c.append(p)
      blap=np.asarray(blap)
      print blap
      for i in range(0,2):
       c[i]=c[i]/float(blap[0][i])
       print float(blap[0][i])
      print c
      with open('SMR_power_left.csv','ab') as f:
 
         cx=csv.writer(f)
         cx.writerow(c)
      if (c[0]>c[1]):
          balx=balx+100*int(c[1]-c[0])
          if balx<10:
              balx=10
      
      
     while(milli1>10000):
        milli1+=clock.tick_busy_loop()
        balx=555
        if(milli1>11000):
         milli1=0
         ir=ir-1
         break
    with open('EEG_Data.csv','ab') as f:
              cx=csv.writer(f)
              cx.writerow('End')
              cx.writerow([])
    pygame.quit()        
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

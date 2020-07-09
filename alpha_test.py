import pygame
from Tkinter import *
from pygame.locals import *
import ctypes
import csv
import numpy as np
from scipy.signal import*
from scipy import*
import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
with open('EEG_Data.csv','ab') as f:

         cx=csv.writer(f)
         cx.writerow('Focus_test')
         cx.writerow([])
with open('Alpha_power_focus_test.csv','wb') as f:

         cx=csv.writer(f)
         
         cx.writerow([])
clock=pygame.time.Clock()
milli1=0
White=(255,255,255)
BLUE=(0,0,255)
Red=(255,0,0)
Black=(0,0,0)
Green=(0,255,0)
pygame.init()
DISPLAYSURF=pygame.display.set_mode((1200,700),pygame.FULLSCREEN)
DISPLAYSURF.fill(White)
def Mbox(title,text,style):
        return ctypes.windll.user32.MessageBoxA(0,text,title,style)

fontObj=pygame.font.Font('freesansbold.ttf',32)

textSurfaceObj1=fontObj.render('Focus',True,BLUE,)
textRectObj=textSurfaceObj1.get_rect()
textRectObj.center=(650,20)
def test(milli1):
                import scipy.io
                mat = scipy.io.loadmat('n1.mat')
                bn= mat['Num1']
                bn=bn[0,:]
                s=0
                p=[]
                a=[]
                av = list(csv.reader(open('Baseline.csv')))   
                data = list(csv.reader(open('Data.csv')))
                ch = [0,30]
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
                 s=s+p
                s=s/2
                print s
                blap = list(csv.reader(open('Alpha_power_baseline.csv')))
                blap=np.asarray(blap)
                print type(blap[0][0])
                print type(s)
                print blap[0][0]
                s=s/float(blap[0][0])
                print s
                with open('Alpha_power_focus_test.csv','ab') as f:

                 cx=csv.writer(f)
                 cx.writerow([s]) 
                mm = list(csv.reader(open('Alpha_power_focus_train.csv')))
                mm=np.hstack(mm)
                mm=max(mm)
                print mm
                nn = list(csv.reader(open('Alpha_power_relax.csv')))
                nn=np.hstack(nn)
                print nn
                nn=max(nn)
                print nn
                mn=0.5*((int(float(mm))+int(float(nn))))
                print mn
                pygame.time.wait(1000) 
                file=csv.reader(open('Alpha_power_focus_test.csv','r'))
                n=[]
                for row in file:
                  n.append(row)                
                n=np.asarray(n[len(n)-1])
                pygame.draw.circle(DISPLAYSURF,White,(650,350),800)
                pygame.draw.circle(DISPLAYSURF,Green,(650,350),abs(int(float(n[len(n)-1]))))
                pygame.draw.circle(DISPLAYSURF,Red,(650,350),int(mn))
                pygame.draw.line(DISPLAYSURF,Black,(630,350),(670,350),10)
                pygame.draw.line(DISPLAYSURF,Black,(650,330),(650,370),10)
                pygame.display.update()            
                print milli1   
                j=0
                print j
                
                return j
while True:
    DISPLAYSURF.fill(White)   
    DISPLAYSURF.blit(textSurfaceObj1,textRectObj)
    milli1+=clock.tick_busy_loop()    
          
    while(milli1<=63000):
        milli1+=clock.tick_busy_loop() 
        j=test(milli1)
        
                     
    if (milli1>=63000):
                with open('EEG_Data.csv','ab') as f:

                 cx=csv.writer(f)
                 cx.writerow('Baseline')
                 cx.writerow([])       

                Mbox('Hello','Testing session Completed.\n Thank you',1)
                '''import os
                os.rename('EEG_Data.csv','EEG_Data'+st+'.csv')
                os.rename('Alpha_power_baseline.csv','Alpha_power_baseline'+st+'.csv')
                os.rename('Baseline.csv','Baseline'+st+'.csv')
                os.rename('Alpha_power_relax.csv','Alpha_power_relax'+st+'.csv')
                os.rename('Alpha_power_focus_train.csv','Alpha_power_focus_train'+st+'.csv')
                os.rename('Alpha_power_focus_test.csv','Alpha_power_focus_test'+st+'.csv')'''
                pygame.quit()
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            
        
        
    pygame.display.update()

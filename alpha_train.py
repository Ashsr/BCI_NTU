
import pygame
from Tkinter import *
from pygame.locals import *
import Baseline
from Baseline import av
import BS_alpha
import ctypes
import csv
import numpy as np
import pygame.mixer
pygame.mixer.init(44100, -16, 2, 2048)
soundObj = pygame.mixer.Sound('beep.wav')
from scipy.signal import*
from scipy import*
import scipy.io
mat = scipy.io.loadmat('n1.mat')
bn= mat['Num1']
bn=np.array(bn)
bn=bn.transpose()
bn=bn[:,0]



clock=pygame.time.Clock()
global va
milli1=0
with open('EEG_Data.csv','ab') as f:

         cx=csv.writer(f)
         cx.writerow('Relax')
         cx.writerow([])
with open('Alpha_power_relax.csv','wb') as f:

         cx=csv.writer(f)
         cx.writerow([])
Red=(225,0,0)
White=(255,255,255)
BLUE=(0,0,255)
Green=(0,255,0)
pygame.init()
#DISPLAYSURF=pygame.display.set_mode((1300,700),pygame.FULLSCREEN)
#DISPLAYSURF.fill(White)
def Mbox(title,text,style):
        return ctypes.windll.user32.MessageBoxA(0,text,title,style)
Mbox('Hello','Please Relax',1)
fontObj=pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj=fontObj.render('Relax',True,BLUE,)
textSurfaceObj1=fontObj.render('Focus',True,BLUE,)
textRectObj=textSurfaceObj.get_rect()
textRectObj.center=(600,20)

while True:

        #DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        p=[]
        a=[]
        s=0
        while(milli1<60000):
         import scipy.io
         mat = scipy.io.loadmat('n1.mat')
         bn= mat['Num1']
         bn=bn[0,:]
         p=[]
         s=0
         a=[]
         pygame.time.wait(1000)
         av = list(csv.reader(open('Baseline.csv')))   
         data = list(csv.reader(open('Data.csv')))
         blap = list(csv.reader(open('Alpha_power_baseline.csv')))
         ch = [0,30]
         y=np.zeros((len(data)-1,2))
         for j in range(0,len(ch)):
          for i in range(0,len(data)-1):
           y[i][j]=float(data[i][ch[j]])-float(av[1][j])
          print shape(y)
          print len(ch)
         for j in range(0,2):
           a=[] 
           for i in range(0,len(data)-1):
            a.append(y[i][j])
           p=convolve(bn,a)
           p=p[:500]
           p=p*p
           p=np.mean(p)         
           s=s+p
           print s    
         s=s/2
         print s
         blap=np.asarray(blap)
         print type(blap[0][0])
         print type(s)
         print blap[0][0]
         s=s/float(blap[0][0])
         print s
         with open('Alpha_power_relax.csv','ab') as f:

            cx=csv.writer(f)
            cx.writerow([s])
         pygame.time.wait(1000)
         milli1+=clock.tick_busy_loop()
        if milli1>=60000:
         with open('EEG_Data.csv','ab') as f:

          cx=csv.writer(f)
          cx.writerow('Baseline')
          cx.writerow([])         
         soundObj.play()
         import time
         time.sleep(1) 
         soundObj.stop()       
         import alpha_train2
         if event.type == QUIT:
            pygame.quit() 
        for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            
        
        
        pygame.display.update()

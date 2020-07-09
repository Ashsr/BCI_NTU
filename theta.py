import pygame
from Tkinter import *
from pygame.locals import *
import ctypes
clock=pygame.time.Clock()
global va
milli1=0
UP='up'
DOWN='down'
va=0.5
Red=(225,0,0)
White=(255,255,255)
BLUE=(0,0,255)
pygame.init()
DISPLAYSURF=pygame.display.set_mode((500,300),0,32)
DISPLAYSURF.fill(White)
pygame.mixer.music.load('Music1.mp3')
pygame.mixer.music.play()
def Mbox(title,text,style):
        return ctypes.windll.user32.MessageBoxA(0,text,title,style)
Mbox('Hello','Training session starts',1)
fontObj=pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj=fontObj.render('Relax and close your eyes',True,BLUE,)
textRectObj=textSurfaceObj.get_rect()
textRectObj.center=(250,100)
while True:
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        

        if milli1==300000:
                Mbox('Hello','Training session Completed.\n Testing session started',1)
        elif milli1==900000:
                Mbox('Hello','Testing session is completed.\n Thank you',1)
        milli1+=clock.tick_busy_loop()

        for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == KEYDOWN:
                 if (event.key==K_UP):
                         if va<1:
                                 va=va+0.1
                                 print va
                                 pygame.mixer.music.set_volume(va)
                                 pygame.draw.rect(DISPLAYSURF,Red,(200,200,100*va,50))
                 elif(event.key==K_DOWN):
                         if va>0:
                                 va=va-0.1
                                 print va
                                 pygame.mixer.music.set_volume(va)
                                 pygame.draw.rect(DISPLAYSURF,White,(90,200,500,500))
                                 pygame.draw.rect(DISPLAYSURF,Red,(200,200,100*va,50))
        
        pygame.display.update()


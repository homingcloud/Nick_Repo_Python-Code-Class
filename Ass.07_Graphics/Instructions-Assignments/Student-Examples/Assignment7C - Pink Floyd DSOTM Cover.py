import pygame, sys

from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1000,1000))

n = 0

RED=(255,0,0)
ORANGE=(255, 128, 0)
YELLOW=(255, 255, 0)
GREEN=(0,255,0)
BLUE=(0,0,255)
VIOLET=(128, 0, 255)

BLACK=(0,0,0)
WHITE=(255,255,255)

screen.fill(BLACK)

#color
while n < 6:
    y1=500
    x2=570
    y2=375
    if n==0:
        COLOR=RED
        y1=485
        x2=570
        y2=390
    if n==1:
        COLOR=ORANGE
        y1=505
        y2=400
    if n==2:
        COLOR=YELLOW
        y1=525
        y2=410
    if n==3:
        COLOR=GREEN
        y1=545
        y2=420
    if n==4:
        COLOR=BLUE
        y1=565
        y2=430
    if n==5:
        COLOR=VIOLET
        y1=585
        y2=440
    pygame.draw.line(screen,COLOR,[1000,y1],[x2,y2],17)
    n=n+1
#prism
pygame.draw.polygon(screen, WHITE,[[500,250],[250,650],[750,650]], 20)
#white light
pygame.draw.line(screen,WHITE,[0,500],[430,401],10)
pygame.draw.polygon(screen, WHITE,[[400, 400],[575, 380],[640,480]])
#finishing
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

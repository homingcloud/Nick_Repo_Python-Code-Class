import pygame, sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1200,600))
fps=60
fpsClock=pygame.time.Clock()
black=(0,0,0)
white=(255,255,255)
c=0
x=400
y=100
direction='down'
while True:
    if c==1:
        direction='right'
        print(c)
    elif c==100:
        direction='down'
        print(c)
    elif c==200:
        direction='left'
        print(c)
    elif c==275:
        direction='up'
        print(c)
    elif c==350:
        direction='right'
        print(c)
    elif c==425:
        direction='down'
        print(c)
    elif c==500:
        direction='left'
        print(c)
    elif c==550:
        direction='up'
        print(c)
    elif c==600:
        direction='right'
        print(c)
    elif c==650:
        direction='down'
        print(c)
    elif c==700:
        direction='left'
        print(c)
    elif c==725:
        direction='up'
        print(c)
        c=0
        x=400
        y=100
    screen.fill(black)
    pygame.draw.circle(screen,white,(x,y),50)
    if direction=='right':
        x=x+2
    elif direction=='left':
        x=x-2
    elif direction=='up':
        y=y-2
    elif direction=='down':
        y=y+2
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    c=c+1
    pygame.display.update()
    fpsClock.tick(fps)

import pygame, sys, time
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,650))
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
t=5
screen.fill(BLACK)
def lrect(a):
    pygame.draw.rect(screen,BLUE,a,50)
def linefunc():
    pygame.draw.line(screen,WHITE,[300,0],[300,650],1)
    pygame.draw.line(screen,WHITE,[600,0],[600,650],1)
    pygame.draw.line(screen,WHITE,[900,0],[900,650],1)

def circle(a):#Circle Fill
    pygame.draw.circle(screen,RED,a,50)
linefunc()
def lcircle(a,c):#Circle Outline
    pygame.draw.circle(screen,RED,a,50,c)
def ldiamond(a,b,c):  
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a+90,b],c)
    a=a+45
    b=b+75
    pygame.draw.line(screen,RED,[a,b],[a-45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a,b],c)
def diamond(a,b):
    c=90
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75])
    while(c>=0):
        pygame.draw.line(screen,RED,[a+45,b-75],[a+c,b])
        pygame.draw.line(screen,RED,[a+45,b+75],[a+c,b])
        pygame.display.update()
        c=c-1
        
screen.fill(BLACK)#Clear Screen
myImg = pygame.image.load('image.png')
screen.blit(myImg, (450,325))




pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

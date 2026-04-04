import pygame, sys, time
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,650))
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
#Screen Drawing
screen.fill(BLACK)
#Functions for Shapes
def linefunc():#Spillting into quadrants
    pygame.draw.line(screen,WHITE,[300,0],[300,650],1)
    pygame.draw.line(screen,WHITE,[600,0],[600,650],1)
    pygame.draw.line(screen,WHITE,[900,0],[900,650],1)
def lrect(a,b,c):#Rectanle Outline
    pygame.draw.rect(screen,BLUE,[a,b,86,147.5],c)
    pygame.display.update()
    time.sleep(1)
    pygame.draw.rect(screen,BLUE,[a,b,86,147.5])
    pygame.display.update()
def lsquare(a,b,c):#Square Outline
    pygame.draw.rect(screen,BLUE,[a,b,90,90],c)
    pygame.display.update()
    time.sleep(1)
    pygame.draw.rect(screen,BLUE,[a,b,90,90])
    pygame.display.update()
def lcircle(a,c):#Circle Outline
    pygame.draw.circle(screen,RED,a,50,c)
    pygame.display.update()
    time.sleep(0.5)
    pygame.draw.circle(screen,RED,a,50)
    pygame.display.update()
def ltri(a,b,c):#Triangle Outline
    pygame.draw.line(screen,RED,[a,b],[a+60,b-100],c)
    pygame.draw.line(screen,RED,[a+60,b-100],[a+120,b],c)
    pygame.draw.line(screen,RED,[a,b],[a+120,b],c)
    pygame.display.update()
    time.sleep(1)
    c=120
    pygame.draw.line(screen,RED,[a,b],[a+60,b-100])
    while(c>=0):
        pygame.draw.line(screen,RED,[a+60,b-100],[a+c,b])
        pygame.display.update()
        c=c-1
    pygame.draw.line(screen,RED,[a,b],[a+120,b])
    pygame.display.update()
def ldiamond(a,b,c):#Diamond Outline 
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a+90,b],c)
    a=a+45
    b=b+75
    pygame.draw.line(screen,RED,[a,b],[a-45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a,b],c)
    pygame.display.update()
    time.sleep(1)
    a=a-45
    b=b-75
    c=90
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75])
    while(c>=0):
        pygame.draw.line(screen,RED,[a+45,b-75],[a+c,b])
        pygame.draw.line(screen,RED,[a+45,b+75],[a+c,b])
        pygame.display.update()
        c=c-1
    pygame.display.update()
t=5#Thickness
#Shapes
linefunc()
squarex=0
y=25
for i in range(6):#Square Outline
    lsquare(x,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lsquare(x+100,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lsquare(x+200,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+100
pygame.draw.line(screen,BLACK,[300,0],[300,650],1)
y=0
recx=300
for i in range(4):#Rectangle Outline
    lrect(x,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lrect(x+106,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lrect(x+212,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+167.5
y=125
trix=600
for i in range(5):#Triangle Outline
    ltri(x,y,t)
    pygame.display.update()
    time.sleep(0.1)
    ltri(x+180,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+124.8
pygame.draw.line(screen,BLACK,[900,0],[900,650],1)
y=100
diamondx=900
for i in range(4):#Diamond Outline
    ldiamond(x,y,t)
    pygame.display.update()
    time.sleep(0.1)
    ldiamond(x+100,y,t)
    pygame.display.update()
    time.sleep(0.1)
    ldiamond(x+200,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+155
time.sleep(3)
screen.fill(BLACK)#Clear Screen
circlex=50
y=75
for i in range(10):#Cicrle Outline
    lcircle([x,y],t)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,y+125],t)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,y+250],t)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,y+325],t)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,y+500],5)
    pygame.display.update()
    time.sleep(0.1)
    x=x+122
time.sleep(3)
screen.fill(BLACK)#Clear Screen
pygame.display.update()
time.sleep(1)
myImg = pygame.image.load('image.png')
screen.blit(myImg, (450,325))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
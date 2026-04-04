
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
def rect(a,b):#Rectangle Fill
    pygame.draw.rect(screen,BLUE,[a,b,86,147.5])
def lsquare(a,b,c):#Square Outline
    pygame.draw.rect(screen,BLUE,[a,b,90,90],c)
def square(a,b):#Square Fill
    pygame.draw.rect(screen,BLUE,[a,b,90,90])
def lcircle(a,c):#Circle Outline
    pygame.draw.circle(screen,RED,a,50,c)
def circle(a):#Circle Fill
    pygame.draw.circle(screen,RED,a,50)
def ltri(a,b,c):#Triangle Outline
    pygame.draw.line(screen,RED,[a,b],[a+60,b-100],c)
    pygame.draw.line(screen,RED,[a+60,b-100],[a+120,b],c)
    pygame.draw.line(screen,RED,[a,b],[a+120,b],c)
def tri(a,b):#Triangle Fill
    c=120
    pygame.draw.line(screen,RED,[a,b],[a+60,b-100])
    while(c>=0):
        pygame.draw.line(screen,RED,[a+60,b-100],[a+c,b])
        pygame.display.update()
        c=c-1
    pygame.draw.line(screen,RED,[a,b],[a+120,b])
def ldiamond(a,b,c):#Diamond Outline 
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a+90,b],c)
    a=a+45
    b=b+75
    pygame.draw.line(screen,RED,[a,b],[a-45,b-75],c)
    pygame.draw.line(screen,RED,[a+45,b-75],[a,b],c)
def diamond(a,b):#Diamond Full
    c=90
    pygame.draw.line(screen,RED,[a,b],[a+45,b-75])
    while(c>=0):
        pygame.draw.line(screen,RED,[a+45,b-75],[a+c,b])
        pygame.draw.line(screen,RED,[a+45,b+75],[a+c,b])
        pygame.display.update()
        c=c-1
t=5#Thickness
#Shapes
linefunc()
y=25
for i in range(6):#Square Outline
    lsquare(0,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lsquare(100,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lsquare(200,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+100
y=0
for i in range(4):#Rectangle Outline
    lrect(300,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lrect(406,y,t)
    pygame.display.update()
    time.sleep(0.1)
    lrect(512,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+167.5
y=25
for i in range(6):#Square Full
    square(0,y)
    pygame.display.update()
    time.sleep(0.1)
    square(100,y)
    pygame.display.update()
    time.sleep(0.1)
    square(200,y)
    pygame.display.update()
    time.sleep(0.1)
    y=y+100
pygame.draw.line(screen,BLACK,[300,0],[300,650],1)
y=0
for i in range(4):#Rectangle Full
    rect(300,y)
    pygame.display.update()
    time.sleep(0.1)
    rect(406,y)
    pygame.display.update()
    time.sleep(0.1)
    rect(512,y)
    pygame.display.update()
    time.sleep(0.1)
    y=y+167.5
y=125
for i in range(5):#Triangle Outline
    ltri(600,y,t)
    pygame.display.update()
    time.sleep(0.1)
    ltri(780,y,t)
    pygame.display.update()
    time.sleep(0.1)
    y=y+124.8
pygame.draw.line(screen,BLACK,[600,0],[600,650],1)
y=100
for i in range(4):#Diamond Outline
    ldiamond(900,y,5)
    pygame.display.update()
    time.sleep(0.1)
    ldiamond(1000,y,5)
    pygame.display.update()
    time.sleep(0.1)
    ldiamond(1100,y,5)
    pygame.display.update()
    time.sleep(0.1)
    y=y+155
y=125
for i in range(5):#Triangle Fill
    tri(600,y)
    pygame.display.update()
    time.sleep(0.1)
    tri(780,y)
    pygame.display.update()
    time.sleep(0.1)
    y=y+124.8
pygame.draw.line(screen,BLACK,[900,0],[900,650],1)
y=100
for i in range(4):#Dimaond Full
    diamond(900,y)
    pygame.display.update()
    time.sleep(0.1)
    diamond(1000,y)
    pygame.display.update()
    time.sleep(0.1)
    diamond(1100,y)
    pygame.display.update()
    time.sleep(0.1)
    y=y+155
time.sleep(3)
screen.fill(BLACK)#Clear Screen
x=50
for i in range(10):#Cicrle Outline
    lcircle([x,75],5)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,200],5)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,325],5)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,450],5)
    pygame.display.update()
    time.sleep(0.1)
    lcircle([x,575],5)
    pygame.display.update()
    time.sleep(0.1)
    x=x+122
x=50
for i in range(10):#Circle Full
    circle([x,75])
    pygame.display.update()
    time.sleep(0.1)
    circle([x,200])
    pygame.display.update()
    time.sleep(0.1)
    circle([x,325])
    pygame.display.update()
    time.sleep(0.1)
    circle([x,450])
    pygame.display.update()
    time.sleep(0.1)
    circle([x,575])
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

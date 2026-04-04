#import some stuff
import random
import math
import pygame, sys
from pygame.locals import*
#set things up
pygame.init()
screen=pygame.display.set_mode((500,500))
#define some colors
#"You might be thinking: how do you make browns contrast enough to be able to
#tell the difference between the ground and sky? Well, I made the sky have more
#green than the ground to give it a yellower look."
SKY=(220,150,50)
SKY2=(180,110,10)
SKYMID=(200,130,38)
GROUND=(90,50,0)
SUN=(255,255,100)
RAYS=(255,200,100)
GROUNDLIGHT=(180,95,25)
GROUNDLIGHT2=(135,72,12)
GROUNDDARK=(60,30,0)
GROUNDDARK2=(30,15,0)
TREE=(45,25,0)
#start drawing
#note: the way I make fades is taking the r, g, b values of the 2 colors
#and averaging them with the same value
screen.fill(SKY)
pygame.draw.rect(screen,SKYMID,[0,50,500,50])
pygame.draw.rect(screen,SKY2,[0,0,500,50])
pygame.draw.polygon(screen,RAYS,[[140,225],[140,235],[50,230]])
pygame.draw.polygon(screen,RAYS,[[160,225],[160,235],[250,230]])
pygame.draw.circle(screen,SUN,(150,230),25)
pygame.draw.rect(screen,GROUND,[0,250,500,250])
pygame.draw.rect(screen,GROUNDLIGHT2,[0,300,500,50])
pygame.draw.rect(screen,GROUNDLIGHT,[0,250,500,50])
pygame.draw.rect(screen,GROUNDDARK,[0,400,500,50])
pygame.draw.rect(screen,GROUNDDARK2,[0,450,500,50])
#THERE CAN NEVER BE ENOUGH VARIABLES
A=0
B=0
global X1
global X2
global X3
global X4
global X5
global XA
global XB
global YA
global YB
X1=10
X2=20
X3=17
X4=12
X5=14
X6=-10
X7=30
X8=-30
X9=70
r=0
XA=X1-20
YA=X1+20
XB=210-10
YB=210+10
#and I wonder where the lag keeps coming from...
while(X2<=500):
    #this makes it so shadows actually conform to perspective/the sun
    #left facing shadows
    if (X1<=50):
        pygame.draw.line(screen,GROUND,[X5,275],[X8,350],9)
    if (X1>=51) and (X1<=125):
        pygame.draw.line(screen,GROUND,[X5,275],[X6,350],9)
    if (X1>125) and (X1<=175):
        #this is the straight shadow since it's in front of the sun
        pygame.draw.line(screen,GROUND,[X5,275],[X5,350],9)
    #right facing shadows
    if (X1>175) and (X1<350):
        pygame.draw.line(screen,GROUND,[X5,275],[X7,350],9)
    if (X1>=350):
        pygame.draw.line(screen,GROUND,[X5,275],[X9,350],9)
    #r is the random distance between the trees (40-60 pixels) 
    r=random.randint(40,60)
    #the actual trees
    pygame.draw.polygon(screen,TREE,[[X1,275],[X2,275],[X3,225],[X3,210],[X4,210],[X4,225]])
    for i in range(10):
        #Y'know what? They're palm trees now! (randomly generated leaves)
        A=random.randint(XA,YA)
        B=random.randint(XB,YB)
        pygame.draw.line(screen,TREE,[X5,210],[A,B],3)
    #MORE VARIABLES
    X1=X1+r
    X2=X2+r
    X3=X3+r
    X4=X4+r
    X5=X5+r
    X6=X6+60
    X7=X7+60
    X8=X8+50
    X9=X9+70
    XA=X1-20
    YA=X1+20
    XB=210-10
    YB=210+10
#all this for some trees..?
#update the display
pygame.display.update()
#quit event
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

import pygame,sys,time, random
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,600))
black=(0,0,0)
dblue=(0,30,80)
blue=(50,160,245)
yellow=(235,235,80)
green=(65,150,40)
brown=(130,75,20)
dbrown=(75,45,10)
gray=(70,70,70)
lgray=(190,190,190)
grass=(40,90,25)
white=(255,255,255)
screen.fill(blue)
pygame.draw.rect(screen,brown,[0,400,1200,50])#dirt
pygame.draw.rect(screen,gray,[0,450,1200,50])#Road
pygame.draw.rect(screen,green,[0,350,1200,50])#Grass Background
pygame.draw.rect(screen,green,[0,400,50,50])#Grass Background
pygame.draw.rect(screen,green,[200,400,800,50])#Grass Background
pygame.draw.rect(screen,green,[1150,400,50,50])#Grass Background
pygame.draw.rect(screen,green,[0,550,1200,50])#Grass Background
for i in range(500):#Individual Grass Loop
    grassy=random.randint(390,425)
    grassx=random.randint(200,1000)
    grassy1=random.randint(330,375)
    grassx1=random.randint(0,1200)
    grassy2=random.randint(530,600)
    pygame.draw.line(screen,grass,[grassx,grassy],[grassx,grassy+25],3)
    pygame.draw.line(screen,grass,[grassx1,grassy1],[grassx1,grassy1+25],3)
    pygame.draw.line(screen,grass,[grassx1,grassy2],[grassx1,grassy2+25],3)
for i in range(25):#Individual Grass Loop #2
    grassx=random.randint(0,50)
    grassx1=random.randint(1150,1200)
    grassy=random.randint(390,425)
    pygame.draw.line(screen,grass,[grassx,grassy],[grassx,grassy+25],3)
    pygame.draw.line(screen,grass,[grassx1,grassy],[grassx1,grassy+25],3)
for i in range(150):#Rocks in dirt
    dirty=random.randint(400,445)
    dirtx=random.randint(50,200)
    dirtx1=random.randint(1000,1150)
    pygame.draw.line(screen,dbrown,[dirtx1,dirty],[dirtx1,dirty+5],3)
    pygame.draw.line(screen,dbrown,[dirtx,dirty],[dirtx,dirty+5],3)
pygame.draw.circle(screen,yellow,(175,500),80)
pygame.draw.rect(screen,gray,[0,500,1200,50])#Road
x=175
for i in range(2):#Tires With symbol
    pygame.draw.circle(screen,black,(x,500),50)#Outer Tire
    pygame.draw.circle(screen,gray,(x,500),30)#2nd Lining
    pygame.draw.circle(screen,lgray,(x,500),20)##Inner Lining
    pygame.draw.circle(screen,dblue,(x,500),15,3)#VW Symbol Outline
    pygame.draw.line(screen,dblue,[x,501],[x-5,508],3)#W
    pygame.draw.line(screen,dblue,[x,501],[x+5,508],3)#W
    pygame.draw.line(screen,dblue,[x-5,508],[x-12,493],3)#W
    pygame.draw.line(screen,dblue,[x+5,508],[x+12,493],3)#W
    pygame.draw.line(screen,dblue,[x,499],[x-5,491],3)#V
    pygame.draw.line(screen,dblue,[x,499],[x+5,491],3)#V
    x=x+300

thx=115
thy=500
#pygame.draw.rect(screen,yellow,[240,500,170,-150])

pygame.display.update()



y=50
for i in range(12):
    pygame.draw.line(screen,black,[0,y],[1200,y],3)
    y=y+50
x=50
for i in range(24):
    pygame.draw.line(screen,black,[x,0],[x,600],3)
    x=x+50
x=125
for i in range(2):# 2 Volkswagen Posts/Signs
    pygame.draw.line(screen,black,[x,230],[x,400],10)#Body Line
    pygame.draw.line(screen,black,[x,400],[x-60,450],10)#Left Leg
    pygame.draw.line(screen,black,[x,400],[x+60,450],10)#Right Leg
    pygame.draw.circle(screen,dblue,(x,175),55,7)#Circle
    pygame.draw.line(screen,dblue,[x,182],[x-25,210],10)#W
    pygame.draw.line(screen,dblue,[x-25,210],[x-50,150],10)#W
    pygame.draw.line(screen,dblue,[x,182],[x+20,210],10)#W
    pygame.draw.line(screen,dblue,[x+20,210],[x+47,150],10)#W
    pygame.draw.line(screen,dblue,[x,175],[x-25,130],10)#V
    pygame.draw.line(screen,dblue,[x+2,175],[x+25,130],10)#V
    x=x+950
x=100
y=60
for i in range(3):# 3 Clouds
    y=y-20
    pygame.draw.ellipse(screen,white,[x,y,125,50])
    pygame.draw.ellipse(screen,white,[x+50,y-30,125,50])
    pygame.draw.ellipse(screen,white,[x+100,y,125,50])
    x=x+350
    y=y+15
    
    





pygame.display.update()

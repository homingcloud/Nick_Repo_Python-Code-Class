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
llgray=(120,120,120)
grass=(40,90,25)
white=(255,255,255)
screen.fill(blue)

def grasss():
    pygame.draw.rect(screen,green,[0,350,1200,50])#Grass Background
    pygame.draw.rect(screen,green,[0,400,50,50])#Grass Background
    pygame.draw.rect(screen,green,[200,400,800,50])#Grass Background
    pygame.draw.rect(screen,green,[1150,400,50,50])#Grass Background
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
def dirt():
    pygame.draw.rect(screen,brown,[0,400,1200,50])#dirt
    for i in range(150):#Rocks in dirt
        dirty=random.randint(400,445)
        dirtx=random.randint(50,200)
        dirtx1=random.randint(1000,1150)
        pygame.draw.line(screen,dbrown,[dirtx1,dirty],[dirtx1,dirty+5],3)
        pygame.draw.line(screen,dbrown,[dirtx,dirty],[dirtx,dirty+5],3)
def tires(x):
    #x=175
    for i in range(2):#Tires With symbol
        pygame.draw.circle(screen,black,(x,500),50)#Outer Tire
        pygame.draw.circle(screen,llgray,(x,500),30)#2nd Lining
        pygame.draw.circle(screen,lgray,(x,500),20)##Inner Lining
        pygame.draw.circle(screen,dblue,(x,500),15,3)#VW Symbol Outline
        pygame.draw.line(screen,dblue,[x,501],[x-5,508],3)#W
        pygame.draw.line(screen,dblue,[x,501],[x+5,508],3)#W
        pygame.draw.line(screen,dblue,[x-5,508],[x-12,493],3)#W
        pygame.draw.line(screen,dblue,[x+5,508],[x+12,493],3)#W
        pygame.draw.line(screen,dblue,[x,499],[x-5,491],3)#V
        pygame.draw.line(screen,dblue,[x,499],[x+5,491],3)#V
        x=x+300
def graph():
    y=50
    for i in range(12):
        pygame.draw.line(screen,black,[0,y],[1200,y],3)
        y=y+50
    x=50
    for i in range(24):
        pygame.draw.line(screen,black,[x,0],[x,600],3)
        x=x+50
def posts():
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
def clouds():#Clouds
    x=100
    y=60
    for i in range(3):# 3 Clouds
        y=y-20
        pygame.draw.ellipse(screen,white,[x,y,125,50])
        pygame.draw.ellipse(screen,white,[x+50,y-30,125,50])
        pygame.draw.ellipse(screen,white,[x+100,y,125,50])
        x=x+350
        y=y+15
def tirecar(x):#Fenders
    for i in range(2):
        pygame.draw.circle(screen,yellow,(x,500),80)
        pygame.draw.circle(screen,gray,(x,500),55)
        x=x+300
def rocks():
    for i in range(150):#Rocks in dirt
        dirty=random.randint(400,445)
        dirtx=random.randint(50,200)
        dirtx1=random.randint(1000,1150)
        pygame.draw.line(screen,dbrown,[dirtx1,dirty],[dirtx1,dirty+5],3)
        pygame.draw.line(screen,dbrown,[dirtx,dirty],[dirtx,dirty+5],3)
def tri(a,b):#Triangle Fill
    c=120
    pygame.draw.line(screen,yellow,[a,b],[a+60,b-100])
    while(c>=0):
        pygame.draw.line(screen,yellow,[a+60,b-100],[a+c,b])
        c=c-1
    pygame.draw.line(screen,yellow,[a,b],[a+120,b])
pygame.draw.rect(screen,gray,[0,450,1200,50])#Road
pygame.draw.rect(screen,brown,[0,400,1200,50])#Dirt
rocks()#Rocks for dirt
grasss()#Top Grass
clouds()#Clouds
posts()#Volkswagen Posts/Signs
tirecar(175)#Car Body #1
tirecar(675)#Car Body #2
pygame.draw.rect(screen,gray,[0,500,1200,50])#Road 
pygame.draw.rect(screen,green,[0,550,1200,50])#Grass Backgroung
for i in range(500):#Individual Grass
    grassy=random.randint(530,600)
    grassx=random.randint(0,1200)
    pygame.draw.line(screen,grass,[grassx,grassy],[grassx,grassy+25],3)
c=0 
y=420
x=485
while (c<=100):#Car Filling Car #1
    pygame.draw.line(screen,yellow,(x,y),(x-120,y-95),1)
    x=x-1
    c=c+1

c=0 
y=420
x=985
while (c<=100):#Car Filling Car #2
    pygame.draw.line(screen,yellow,(x,y),(x-120,y-95),1)
    x=x-1
    c=c+1
tires(175)#Volkswagen Tires Car #1
tires(675)#Volkswagen Tires Car #2
tri(175,425)#Car Body Back Car #1
tri(675,425)#Car Body Back Car #2
#Car #1 Filling
pygame.draw.rect(screen,yellow,[200,400,250,50])#Car Filling #1
pygame.draw.rect(screen,yellow,[400,410,70,30])#Car Filling #1
pygame.draw.rect(screen,yellow,[350,450,70,50])#Car Filling #1
pygame.draw.rect(screen,yellow,[235,325,130,175])#Car Filling #1
#Car #2 Filling
pygame.draw.rect(screen,yellow,[700,400,250,50])#Car Filling #2
pygame.draw.rect(screen,yellow,[900,410,70,30])#Car Filling #2
pygame.draw.rect(screen,yellow,[850,450,70,50])#Car Filling #2
pygame.draw.rect(screen,yellow,[735,325,130,175])#Car Filling #2
#Car #1 Window Outline
pygame.draw.line(screen,black,[365,340],[450,415],5)#Windows Outline Car #1
pygame.draw.line(screen,black,[310,340],[365,340],5)#Windows Outline Car #1
pygame.draw.line(screen,black,[310,340],[310,415],5)#Windows Outline Car #1
pygame.draw.line(screen,black,[310,415],[450,415],5)#Windows Outline Car #1
#Car #2 Window Outline
pygame.draw.line(screen,black,[365+500,340],[450+500,415],5)#Windows Outline Car #2
pygame.draw.line(screen,black,[310+500,340],[365+500,340],5)#Windows Outline Car #2
pygame.draw.line(screen,black,[310+500,340],[310+500,415],5)#Windows Outline Car #2
pygame.draw.line(screen,black,[310+500,415],[450+500,415],5)#Windows Outline Car #2

c=140
x=450
y=415
while(c!=0):#Car #1 Window Filling
    pygame.draw.line(screen,black,[365,340],[x,415],5)
    pygame.draw.line(screen,black,[365,340],[310,y],5)
    x=x-1
    y=y-0.5
    c=c-1
    
c=140
x=950
y=415
while(c!=0):#Car #2 Window Filling
    pygame.draw.line(screen,black,[865,340],[x,415],5)
    pygame.draw.line(screen,black,[865,340],[810,y],5)
    x=x-1
    y=y-0.5
    c=c-1
#graph()
pygame.display.update()

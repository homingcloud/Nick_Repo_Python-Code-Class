import pygame,sys,random
from pygame.locals import*
pygame.init()
fps=60
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600))

white=(255,255,255)
black=(0,0,0)
dblue=(0,30,80)

def VW(x,y):
    pygame.draw.circle(screen,dblue,(x,y),15,3)#VW Symbol Outline
    pygame.draw.line(screen,dblue,[x,y+1],[x-5,y+8],3)#W
    pygame.draw.line(screen,dblue,[x,y+1],[x+5,y+8],3)#W
    pygame.draw.line(screen,dblue,[x-5,y+8],[x-12,y-7],3)#W
    pygame.draw.line(screen,dblue,[x+5,y+8],[x+12,y-7],3)#W
    pygame.draw.line(screen,dblue,[x,y-1],[x-5,y-9],3)#V
    pygame.draw.line(screen,dblue,[x,y-1],[x+5,y-9],3)#V

x=random.randint(15,1185)
x1=random.randint(15,1185)
x2=random.randint(15,1185)
x3=random.randint(15,1185)
x4=random.randint(15,1185)
x5=random.randint(15,1185)
x6=random.randint(15,1185)
y=-15
y1=-15
y2=-15
y3=-15
y4=-15
y5=-15
y6=-15

time=0
speed=3

while True:
    screen.fill(white)
    VW(x,y)
    if time>=100 or y1>15:
        VW(x1,y1)
        y1=y1+speed
    if time>=200 or y2>15:
        VW(x2,y2)
        y2=y2+speed
    if time>=300 or y3>15:
        VW(x3,y3)
        y3=y3+speed
    if time>=400 or y4>15:
        VW(x4,y4)
        y4=y4+speed
    if time>=500 or y5>15:
        VW(x5,y5)
        y5=y5+speed
    if time>=600 or y6>15:
        VW(x6,y6)
        y6=y6+speed
    if time>=650:
        time=0
    if y>=610:
        y=-15
        x=random.randint(15,1185)
    if y>=610:
        y=-15
        x=random.randint(15,1185)
    if y1>=610:
        y1=-15
        x1=random.randint(15,1185)
    if y2>=610:
        y2=-15
        x2=random.randint(15,1185)
    if y3>=610:
        y3=-15
        x3=random.randint(15,1185)
    if y4>=610:
        y4=-15
        x4=random.randint(15,1185)
    if y5>=610:
        y5=-15
        x5=random.randint(15,1185)
    if y6>=610:
        y6=-15
        x6=random.randint(15,1185)
    y=y+speed
    time=time+5
    pygame.display.update()
    fpsClock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    


import pygame,sys,random,time
from pygame.locals import*

pygame.init()
fps=30
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600))

white=(255,255,255)
black=(0,0,0)
dblue=(0,30,80)
green=(97,233,100)
red=(204,2,2)

def VW(a,b,c):
    pygame.draw.circle(screen,c,(a,b),25)#Outer Symbol Outline
    pygame.draw.circle(screen,white,(a,b),21,2)#Inner Symbol Outline
    pygame.draw.rect(screen,white,[a-2.5,b,5,12],4)
    pygame.draw.rect(screen,white,[a-2.5,b,5,-10],4)
    pygame.draw.rect(screen,white,[a-2.5,b-2.5,15,5],4)
    pygame.draw.rect(screen,white,[a-2.5,b-2.5,-9,5],4)
    

    

move_left=False
move_right=False
move_down=False
move_up=False
gr=False

xu=600
yu=300
x=random.randint(15,115)
x1=random.randint(215,215)
x2=random.randint(315,315)
x3=random.randint(415,415)
x4=random.randint(515,515)
x5=random.randint(615,615)
x6=random.randint(715,715)
x7=random.randint(815,815)
x8=random.randint(915,915)
x9=random.randint(1015,1015)
x10=random.randint(1115,1115)
x11=random.randint(15,1185)
x12=random.randint(15,1185)
gx=random.randint(15,1185)
g1x=random.randint(15,1185)
y=-30
y1=-30
y2=-30
y3=-30
y4=-30
y5=-30
y6=-30
y7=-30
y8=-30
y9=-30
y10=-30
y11=-30
y12=-30
gy=-30
time=0
ptime=0
fallspeed=5
uspeed=10
uwidth=15
raincolor=red
snum=-15
while True:    
    screen.fill(white)
    ###############################Scoring Code
    # if touches break
    ################################USER/PLAYER
    if xu<=15:
        xu=15
    elif xu>=1200:
        xu=1200-uwidth
    if yu<=uwidth:
        yu=uwidth
    elif yu>=600:
        yu=600-uwidth
    VW(xu,yu,dblue)
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        xu=xu-uspeed
    if keys[K_RIGHT]:
        xu=xu+uspeed
    if keys[K_UP]:
        yu=yu-uspeed
    if keys[K_DOWN]:
        yu=yu+uspeed
    ################################Green Code
    if ptime==3:
        gr=True
    if gr==True:
        if gy<=610:
            VW(gx,gy,green)
            VW(g1x,gy,green)
            gy=gy+fallspeed
        if gy>=610:
            gr=False
            gy=-15
            gx=random.randint(15,1185)
            g1x=random.randint(15,1185)
            ptime=0

    ####################################RAIN/ANTAGONISTS
    VW(x,y,raincolor)
    if time>=100 or y1>=-15 or y7>=-15:
        VW(x1,y1,raincolor)
        y1=y1+fallspeed
        VW(x7,y7,raincolor)
        y7=y7+fallspeed
    if time>=400 or y5>=-15 or y11>=-15:
        VW(x5,y5,raincolor)
        y11=y11+fallspeed
        VW(x11,y11,raincolor)
        y11 += fallspeed
    if time>=700 or y3>=-15 or y9>=-15:
        VW(x3,y3,raincolor)
        y3=y3+fallspeed
        VW(x9,y9,raincolor)
        y9=y9+fallspeed
    if time>=1000 or y6>=-15 or y12>=-15:
        VW(x6,y6,raincolor)
        y6=y6+fallspeed
        VW(x12,y12,raincolor)
        y12=y12+fallspeed
    if time>=1300 or y2>=-15 or y8>=-15:
        VW(x2,y2,raincolor)
        y2=y2+fallspeed
        VW(x8,y8,raincolor)
        y8=y8+fallspeed
    if time>=1600 or y4>=-15 or y10>=-15:
        VW(x4,y4,raincolor)
        y4=y4+fallspeed
        VW(x10,y10,raincolor)
        y10=y10+fallspeed
    if time>=1700:
        time=0
    if y>=610:
        y=-15
        ptime=ptime+1
        snum=snum+1
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
        x5=random.randint(15,615)
    if y6>=610:
        y6=-15
        x6=random.randint(15,1185)
    if y7>=610:
        y7=-15
        x7=random.randint(15,1185)
    if y8>=610:
        y8=-15
        x8=random.randint(15,1185)
    if y9>=610:
        y9=-15
        x9=random.randint(15,1015)
    if y10>=610:
        y10=-15
        x10=random.randint(15,1185)
    if y11>=610:
        y11=-15
        x11=random.randint(15,1185)
    y=y+fallspeed
    time=time+fallspeed
    pygame.display.update()
    fpsClock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

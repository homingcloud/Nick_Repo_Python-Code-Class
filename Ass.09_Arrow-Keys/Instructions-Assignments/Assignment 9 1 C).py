import pygame,sys,random,time,math
from pygame.locals import*

pygame.init()
fps=60
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))

white=(255,255,255)
black=(0,0,0)
dblue=(0,30,80)
green=(97,233,100)
red=(204,2,2)
heartt=False
def VW(x,y,c):
    pygame.draw.circle(screen,c,(x,y),15,3)#VW Symbol Outline
    pygame.draw.line(screen,c,[x,y+1],[x-5,y+8],3)#W
    pygame.draw.line(screen,c,[x,y+1],[x+5,y+8],3)#W
    pygame.draw.line(screen,c,[x-5,y+8],[x-12,y-7],3)#W
    pygame.draw.line(screen,c,[x+5,y+8],[x+12,y-7],3)#W
    pygame.draw.line(screen,c,[x,y-1],[x-5,y-9],3)#V
    pygame.draw.line(screen,c,[x,y-1],[x+5,y-9],3)#V


heartimg1=pygame.image.load('pixelheart.jpg').convert()
heartimg1=pygame.transform.scale(heartimg1,(65,65))
heartimg2=pygame.image.load('pixelheart.jpg').convert()
heartimg2=pygame.transform.scale(heartimg2,(65,65))
heartimg3=pygame.image.load('pixelheart.jpg').convert()
heartimg3=pygame.transform.scale(heartimg3,(65,65))
nonheartimg=pygame.image.load('nonheart.jpg').convert()
nonheartimg=pygame.transform.scale(nonheartimg,(65,65))
heartimg=pygame.image.load('pixelheart.jpg').convert()
heartimg=pygame.transform.scale(heartimg,(65,65))


move_left=False
move_right=False
move_down=False
move_up=False
go=False
go1=False
score=0
xu=600
yu=300
x=random.randint(25,125)
x1=random.randint(125,225)
x2=random.randint(225,325)
x3=random.randint(325,425)
x4=random.randint(425,525)
x5=random.randint(525,625)
x6=random.randint(625,725)
x7=random.randint(725,800)
x8=random.randint(25,800)
x9=random.randint(25,800)
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
gy=-30
g1y=-30
time1=0
ptime=0
fallspeed=4
uspeed=6
uwidth=15
raincolor=red
snum=-15
hearts=3
heart=0
no=0
hno=0
h1no=0
n1o=0
question=0
def restart():
    global y,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12
    global gy,g1y,time1,ptime
    y=y1=y2=y3=y4=y5=y6=y7=y8=y9=y10=y11=y12=-30
    gy=g1y=-30
    time1=ptime=0

while hearts!=-1:    
    screen.fill(white)
    if xu<=15:
        xu=15
    elif xu>=800-uwidth:
        xu=800-uwidth
    if yu<=uwidth:
        yu=uwidth
    elif yu>=600-uwidth:
        yu=600-uwidth
    ###############################Hearts Code
    screen.blit(heartimg1,(10,10))
    screen.blit(heartimg2,(75,10))
    screen.blit(heartimg3,(140,10))
    while heartt==True:
            if hearts==2:
                for i in range(4):
                    heartimg3=nonheartimg
                    screen.blit(heartimg3,(140,10))
                    pygame.display.update()
                    time.sleep(0.4)
                    heartimg3=heartimg
                    screen.blit(heartimg3,(140,10))
                    pygame.display.update()
                    time.sleep(0.4)
                heartt=False
            elif hearts==1:
                for i in range(4):
                    heartimg2=nonheartimg
                    screen.blit(heartimg2,(75,10))
                    pygame.display.update()
                    time.sleep(0.4)
                    heartimg2=heartimg
                    screen.blit(heartimg2,(75,10))
                    pygame.display.update()
                    time.sleep(0.4)
                heartt=False
            elif hearts==0:
                for i in range(4):
                    heartimg1=nonheartimg
                    screen.blit(heartimg1,(10,10))
                    pygame.display.update()
                    time.sleep(0.4)
                    heartimg1=heartimg
                    screen.blit(heartimg1,(10,10))
                    pygame.display.update()
                    time.sleep(0.4)
                heartt=False
                hearts=hearts-1
                screen.fill(white)
    if hearts>3:
        hearts=hearts-1
    if hearts==3:
        heartimg3=heartimg
        heartimg2=heartimg
        heartimg1=heartimg
    if hearts==2:
        heartimg3=nonheartimg
        heartimg2=heartimg
        heartimg1=heartimg
    if hearts==1:
        heartimg1=heartimg
        heartimg2=nonheartimg
        heartimg3=nonheartimg
    if hearts==0:
        heartimg1=nonheartimg
        heartimg3=nonheartimg
        heartimg2=nonheartimg
    
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
        
    if score>=500:
        fallspeed=6
    if score>=900:
        fallspeed=8
    if score>=1200:
        fallspeed=10
    if score>=1400:
        fallspeed=12
    ################################Green/Hearts/Scoring Code
    if ptime==2:
        go=True
    if ptime==3:
        go1=True
        go=False
    if ptime==4:
        go1=False
        ptime=0
    if go is True:
        if gy<610:
            VW(gx,gy,green)
            gy=gy+fallspeed
            if math.hypot((xu-gx),(yu-gy))<30:
                if hearts<3:
                    hearts=hearts+1
                    hno=hno+1
                    if hno>1:
                        hearts=hearts-1
                else:
                    score=score+100
                    no=no+1
                    if no>1:
                        score=score-100
        else:
            gy=-15
            gx=random.randint(15,1185)
            no=0
            hno=0
    if go1 is True:
        if g1y<610:
            VW(g1x,g1y,green)
            g1y=g1y+fallspeed
            if math.hypot((xu-g1x),(yu-g1y))<30:
                if hearts<3:
                    hearts=hearts+1
                    h1no=h1no+1
                    if h1no>1:
                        hearts=hearts-1
                else:
                    score=score+100
                    n1o=n1o+1
                    if n1o>1:
                        score=score-100
        else:
            g1y=-15
            g1x=random.randint(15,1185)
            n1o=0
            h1no=0
    ####################################RAIN/ANTAGONISTS
    VW(x,y,raincolor)
    if time1>=100 or y1>=-15 or y8>=-15:
        VW(x1,y1,raincolor)
        y1=y1+fallspeed
        if time1>=135 or y8>=-15:
            VW(x8,y8,raincolor)
            y8=y8+fallspeed
    if time1>=400 or y3>=-15 or y4>=-15:
        VW(x4,y4,raincolor)
        y4=y4+fallspeed
        if time1>=435 or y3>=-15:
            VW(x3,y3,raincolor)
            y3+=fallspeed
    if time1>=700 or y5>=-15 or y6>=-15:
        VW(x5,y5,raincolor)
        y5=y5+fallspeed
        if time1>=735 or y9>=-15:
            VW(x6,y6,raincolor)
            y6=y6+fallspeed
    if time1>=1000 or y7>=-15 or y2>=-15:
        VW(x7,y7,raincolor)
        y7=y7+fallspeed
        if time1>=1035 or y2>=-15:
            VW(x2,y2,raincolor)
            y2=y2+fallspeed
    if time1>=1300 or y9>=-15:
        VW(x9,y9,raincolor)
        y9=y9+fallspeed
    if math.hypot((x-xu),(y-yu))<45:
        hearts=hearts-1
        heartt=True
        y=-15
    elif math.hypot((x1-xu),(y1-yu))<30:
        hearts=hearts-1
        heartt=True
        y1=-15
    elif math.hypot((x2-xu),(y2-yu))<30:
        hearts=hearts-1
        heartt=True
        y2=-15
    elif math.hypot((x3-xu),(y3-yu))<30:
        hearts=hearts-1
        heartt=True
        y3=-15
    elif math.hypot((x4-xu),(y4-yu))<30:
        hearts=hearts-1
        heartt=True
        y4=-15
    if math.hypot((x5-xu),(y5-yu))<30:
        hearts=hearts-1
        heartt=True
        y5=-15
    if math.hypot((x6-xu),(y6-yu))<30:
        hearts=hearts-1
        heartt=True
        y6=-15
    if math.hypot((x7-xu),(y7-yu))<30:
        hearts=hearts-1
        heartt=True
        y7=-15
    if math.hypot((x8-xu),(y8-yu))<30:
        hearts=hearts-1
        heartt=True
        y8=-15
    if math.hypot((x9-xu),(y9-yu))<30:
        hearts=hearts-1
        heartt=True
        y9=-15
    if time1>=1700:
        time1=0
    if y>=610:
        y=-15
        ptime=ptime+1
        x=random.randint(25,125)
        score=score+1
        question=question+1
    if y1>=610:
        y1=-15
        x1=random.randint(125,225)
        score=score+1
    if y2>=610:
        y2=-15
        x2=random.randint(225,325)
        score=score+1
    if y3>=610:
        y3=-15
        x3=random.randint(325,425)
        score=score+1
    if y4>=610:
        y4=-15
        x4=random.randint(425,525)
        score=score+1
    if y5>=610:
        y5=-15
        x5=random.randint(525,625)
        score=score+1
    if y6>=610:
        y6=-15
        x6=random.randint(625,725)
        score=score+1
    if y7>=610:
        y7=-15
        x7=random.randint(725,825)
        score=score+1
    if y8>=610:
        y8=-15
        x8=random.randint(825,925)
        score=score+1
    if y9>=610:
        y9=-15
        x9=random.randint(925,1025)
        score=score+1
    y=y+fallspeed
    time1=time1+fallspeed
    pygame.display.update()
    fpsClock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
screen.fill(white)
pygame.display.update()
print('Good job playing this program\nYour final score is',score)




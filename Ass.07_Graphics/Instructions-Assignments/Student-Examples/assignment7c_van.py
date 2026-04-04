import pygame, sys
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((1400,800))

RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
YELLOW=(255, 255, 0)
Tree1=(0,128,0)
Tree2=(31,204,51)
Wood=(153,102,51)
Sky=(153,204,255)
Grass=(153,255,102)
house=(255,153,153)
house2=(255,102,153)
door=(255,204,255)
win=(204,153,255)
mountain=(100,100,100)
#3. Draw things
screen.fill(Sky)
pygame.draw.polygon(screen, mountain, [[0,100 ], [150, 250],[210,150],[300,300],[420,80],[500,200],[630,10],[730,200],[900,40],[1030,200],[1200,20],[1300,230],[1500,50],[1500,750],[0,750]])
pygame.draw.rect(screen, Grass,[0,500,1400,300])

y=350
count=0
for x in range(400,1500,70):
    if count%2==0:
        color=Tree1
        y=y+5
    else:
        color=Tree2
        y=y-5
    pygame.draw.polygon(screen, color, [[x, y], [x-50, y+100],[x+50,  y+100]])
    pygame.draw.polygon(screen, color, [[x, y+33], [x-50, y+100+33],[x+50,  y+100+33]])
    pygame.draw.polygon(screen, color, [[x, y+66], [x-50, y+100+66],[x+50,  y+100+66]])
    pygame.draw.rect(screen, Wood,[x-10,y+166,20,20])
    count=count+1


pygame.draw.polygon(screen, house2, [[650,200 ], [350, 450],[910,450]])
pygame.draw.rect(screen, house,[500,450,350,320])
pygame.draw.rect(screen, door,[620,600,100,170])
pygame.draw.rect(screen, win,[630,480,120,90])



pygame.draw.ellipse(screen, BLUE,[900,570,450,200])


y=250
count=0
for x in range(100,500,100):
    if count%2==0:
        color=Tree1
    else:
        color=Tree2

    pygame.draw.polygon(screen, color, [[x, y], [x-150, y+300],[x+150,  y+300]])
    pygame.draw.polygon(screen, color, [[x, y+100], [x-150, y+300+100],[x+150,  y+300+100]])
    pygame.draw.polygon(screen, color, [[x, y+200], [x-150, y+300+200],[x+150,  y+300+200]])
    pygame.draw.rect(screen, Wood,[x-25,y+300+200,50,50])
    count=count+1

    
pygame.display.update()  #update image

#4. Add a loop so that the screen stays visible until you click the x to close the program
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

#import random
import random
#import pygame and initialize the screen
import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1100,500))
#variables
treenum=0
treereset=0
starnum=0
starreset=0
trunk1=-30
trunk2=230
trunk3=10
trunk4=20
leaf1=-45
leaf2=230
leaf3=-5
leaf4=230
leaf5=-25
leaf6=190
star1=-100
star2=5
#colours
LIGHTYELLOW=(253,234,96)
SUNSETORANGE=(253,102,2)
SUNSETPINK=(208,51,122)
DARKINDIGO=(22,0,113)
DARKBLUE=(0,0,26)
BLACK=(0,0,0)
SUN=(253,222,2)
STAR=(254,247,192)
GRASS=(29,69,10)
TRUNK=(57,28,6)
LEAVES=(3,26,0)

#draw!!
#tree function
def drawtree (a,b,c,d,e,f,g,h,i,j):
    trunk=pygame.draw.rect(screen,TRUNK,[a,b,c,d])
    leaves=pygame.draw.polygon(screen,LEAVES,[[e,f],[g,h],[i,j]])
    return trunk,leaves
#star function
def drawstar (a,b,c):
    star=pygame.draw.circle(screen,STAR,[a,b],c)
#sunset
pygame.draw.rect(screen,BLACK,[0,0,1100,500])#background
pygame.draw.circle(screen,DARKBLUE,[550,500],650)#dark blue circle
pygame.draw.circle(screen,DARKINDIGO,[550,500],600)#dark indigo circle
pygame.draw.circle(screen,SUNSETPINK,[550,500],550)#pink circle
pygame.draw.circle(screen,SUNSETORANGE,[550,500],500)#orange circle
pygame.draw.circle(screen,SUN,[550,500],450)#dark yellow circle
pygame.draw.circle(screen,LIGHTYELLOW,[550,500],400)#light yellow circle
#star
while starnum<70 and starreset<50:
    #random number
    rnum2=random.randint(50,100)
    #draw star
    drawstar(star1,star2,2)
    #change star placement
    star1=star1+rnum2
    #count star
    starnum=starnum+1
    #make the other lines
    if (starnum==49 and starreset<50):
        star1=-100
        star2=star2+5
        starnum=0
        starreset=starreset+1
#pygame.draw.circle(screen,LIGHTYELLOW,[5,5],4)
#sun
pygame.draw.circle(screen,SUN,[550,250],100)
#grass
pygame.draw.rect(screen,GRASS,[0,250,1100,500])#grass
#tree test
pygame.draw.rect(screen,TRUNK,[-30,230,10,20])
pygame.draw.polygon(screen,LEAVES,[[-45,230],[-5,230],[-25,190]])
#make those trees
while treenum<22 and treereset<12:
    #draw tree
    drawtree(trunk1,trunk2,trunk3,trunk4,leaf1,leaf2,leaf3,leaf4,leaf5,leaf6)
    #random number things
    rnum=random.randint(40,80)
    #change tree placement
    trunk1=trunk1+rnum
    leaf1=leaf1+rnum
    leaf3=leaf3+rnum
    leaf5=leaf5+rnum
    #count the tree
    treenum=treenum+1
    #make the other lines
    if (treenum==21 and treereset<12):
        trunk1=-30
        trunk2=trunk2+30
        trunk3=10
        trunk4=20
        leaf1=-45
        leaf2=leaf2+30
        leaf3=-5
        leaf4=leaf4+30
        leaf5=-25
        leaf6=leaf6+30
        treereset=treereset+1
        treenum=0
#update image
pygame.display.update() #update image
#loop to keep the screen
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    

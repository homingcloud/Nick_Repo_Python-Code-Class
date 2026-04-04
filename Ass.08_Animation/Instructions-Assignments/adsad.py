import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,600))
fps=30
fpsClock=pygame.time.Clock()
black=(0,0,0)
white=(255,255,255)
x=760
y=95
direction='left'
backgroundimg=pygame.image.load('background.JPG')
backgroundimg=pygame.transform.scale(backgroundimg,(1200,600))

carileft=pygame.image.load('Carleft.JPG').convert()
carileft=pygame.transform.scale(carileft,(210,60))

cariturnin=pygame.image.load('Carturnin.JPG').convert()
cariturnin=pygame.transform.scale(cariturnin,(190,60))

caristraight=pygame.image.load('Carstraight.JPG').convert()
caristraight=pygame.transform.scale(caristraight,(125,60))

cariturnout=pygame.image.load('Carturnout.JPG').convert()
cariturnout=pygame.transform.scale(cariturnout,(190,60))

cariright=pygame.image.load('Carright.JPG').convert()
cariright=pygame.transform.scale(cariright,(210,60))

def graph():
    y=50
    for i in range(12):
        pygame.draw.line(screen,black,[0,y],[1200,y],3)
        y=y+50
    x=50
    for i in range(24):
        pygame.draw.line(screen,black,[x,0],[x,600],3)
        x=x+50
image=carileft
while True:
    #print('x:',x,'y:',y)
    if x<=230 and y<150:
        image=cariturnin
        direction='turnin'
    elif x<100 and y<225 :
        image=caristraight
        direction='straight'
    elif y>340 and x<350:
        image=cariturnout
        direction='turnout'
    elif x==357 and y==446:
        image=cariright
        direction='right'
    elif x>585 and y==446:
        direction='stop'

    screen.fill(black)
    screen.blit(backgroundimg,(0,0))
    screen.blit(image,(x,y))
    #graph()
    if direction=='left':
        x=x-3
    elif direction=='right':
        x=x+3
    elif direction=='turnin':
        x=x-8
        y=y+3
    elif direction=='straight':
        y=y+3
    elif direction=='turnout':
        x=x+8
        y=y+3
    elif direction=='stop':
        y=y-0
        x=x-0
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
        

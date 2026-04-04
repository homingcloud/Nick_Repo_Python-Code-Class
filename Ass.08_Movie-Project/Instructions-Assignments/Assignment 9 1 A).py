import pygame,sys
from pygame.locals import*
pygame.init()
fps=30
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600))
white=(255,255,255)
black=(0,0,0)
dblue=(0,30,80)
x=1100
y=0
move_left=False
move_right=False
move_down=False
move_up=False
speed=10
width=15
def VW(x,y):
    pygame.draw.circle(screen,dblue,(x,y),15,3)#VW Symbol Outline
    pygame.draw.line(screen,dblue,[x,y+1],[x-5,y+8],3)#W
    pygame.draw.line(screen,dblue,[x,y+1],[x+5,y+8],3)#W
    pygame.draw.line(screen,dblue,[x-5,y+8],[x-12,y-7],3)#W
    pygame.draw.line(screen,dblue,[x+5,y+8],[x+12,y-7],3)#W
    pygame.draw.line(screen,dblue,[x,y-1],[x-5,y-9],3)#V
    pygame.draw.line(screen,dblue,[x,y-1],[x+5,y-9],3)#V
while True:
    screen.fill(white)
    if x<=15:
        x=15
    elif x>=1200:
        x=1200-width
    if y<=width:
        y=width
    elif y>=600:
        y=600-width
    VW(x,y)
    ############################
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        x=x-speed
    if keys[K_RIGHT]:
        x=x+speed
    if keys[K_UP]:
        y=y-speed
    if keys[K_DOWN]:
        y=y+speed
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)

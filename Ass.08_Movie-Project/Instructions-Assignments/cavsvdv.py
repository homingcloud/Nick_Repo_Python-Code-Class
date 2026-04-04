import pygame, sys
from pygame.locals import *
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600))
white=(255, 255, 255)
black=(0,0,0)
tx=1100
ty=0
move_left = False
move_right = False
move_up = False
move_down = False
speed=30
while True:
     screen.fill(white)
     if tx<=0:
         tx=0
     if ty==-speed:
        ty +=speed
     if tx>=1200:
        tx=1200-25
     if ty>=600:
         ty=600
        
     print('x=',tx,'y=',ty)
     pygame.draw.line(screen,black,[tx,ty],[tx+25,ty],5)
     #--------------------------------------------------------------
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
         keys=pygame.key.get_pressed()
         if keys[K_LEFT]:
             tx -= speed
         if keys[K_RIGHT]:
             tx += speed
         if keys[K_UP]:
             ty -= speed
         if keys[K_DOWN]:
             ty += speed
        
            
     pygame.display.update()   
     fpsClock.tick(FPS)   

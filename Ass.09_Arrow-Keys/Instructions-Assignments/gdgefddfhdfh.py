import pygame, sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,600))
white=(255,255,255)
black=(0,0,0)
lightr=(190,105,65)
while True:
    screen.fill(white)
    pygame.draw.rect(screen,lightr,[0,0,1200,250])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

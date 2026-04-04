#import and initialize
import pygame, sys, math
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600)) #screen size

#declare colours
BACK = (150,150,150)
BLACK = (0,0,0)
BODY = (30,220,60)
WHITE = (255,255,255)
BODY2 = (0,170,45)
CLOTHES = (100,10,100)
RGB = [(255,0,0),(0,255,0),(0,0,255)]
GOLD = (255,215,0)

#draw some things
screen.fill(BACK) #background
#frog
pygame.draw.polygon(screen,CLOTHES,[[220,350],[380,350],[450,600],[150,600]]) #clothes
pygame.draw.polygon(screen,GOLD,[[200,400],[400,400],[300,500]],6) #chain
pygame.draw.ellipse(screen,BODY,[160,235,280,200]) #head
pygame.draw.circle(screen,BODY,(225,250),65) #eye socket thing 1
pygame.draw.circle(screen,BODY,(375,250),65) #eye socket thing 2
pygame.draw.circle(screen,BODY2,(225,250),51) #eyeball outline 1
pygame.draw.circle(screen,BODY2,(375,250),51) #eyeball outline 2
pygame.draw.circle(screen,WHITE,(225,250),46) #eyeball 1
pygame.draw.circle(screen,WHITE,(375,250),46) #eyeball 2
pygame.draw.circle(screen,BODY2,(300,275),10) #cool circle 1
pygame.draw.circle(screen,BODY2,(300,325),10) #cool circle 2
pygame.draw.ellipse(screen,BODY2,[230,360,140,65],5) #mouth
for i in range(3):
    pygame.draw.circle(screen,BLACK,(225,250),(i+1) * 10,round((i+2)/2)) #make a bunch of circles, increasing the radius and width
    pygame.draw.circle(screen,BLACK,(375,250),(i+1) * 10,round((i+2)/2)) #make a bunch of circles, increasing the radius and width
#orb
for i in range(45):
    pygame.draw.circle(screen,RGB[i%3],(300,490),(46-(i+1))) #make a bunch of circles, decreasing the radius and change color
#done
pygame.display.update() #update the screen

#make it visible
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

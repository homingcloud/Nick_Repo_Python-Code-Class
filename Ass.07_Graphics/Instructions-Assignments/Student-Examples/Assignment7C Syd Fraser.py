#IMPORT
import pygame,sys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1100,800))

#COLOURS
ORANGE=(229,121,85)
SHORANGE=(213,103,66)
DORANGE=(187,83,49)
LBLACK=(20,22,28)
BLACK=(0,0,0)
PAWS=(14,16,22)
CANDLE=(207,195,170)
FLAME=(245,144,71)
YELLOW=(255,237,108)
GLOW=(255,229,139)
GLOW2=(52,46,23)
WHITE=(223,216,216)
NOSE=(193,92,92)
SHGRASS=(44,66,49)
GRASS=(90,145,101)

#START
#while True:
#screen.fill(BLACK)
#CAT
pygame.draw.circle(screen,LBLACK,(550,260),120)#HEAD
#GLOW/SHADOW
pygame.draw.ellipse(screen,GLOW2,[475,0,150,140])#CANDLE BGLOW
pygame.draw.circle(screen,GLOW,(550,70),50)#CANDLE DGLOW

#pygame.draw.ellipse(screen,GLOW,[350,680,800,200])#SHADOW GLOW
#pygame.draw.ellipse(screen,GLOW2,[300,680,700,140])#SHADOW GLOW
#CANDLE
pygame.draw.line(screen,LBLACK,[552,98],[552,70],3)#CANDLE LINE
pygame.draw.rect(screen,CANDLE,[527,98,50,60])#CANDLE
pygame.draw.ellipse(screen,CANDLE,[515,140,70,40])#DRIP
pygame.draw.line(screen,CANDLE,[548,150],[548,200],5)#LONG DRIP
pygame.draw.line(screen,CANDLE,[525,150],[525,225],5)#LONG DRIP
#CAT
pygame.draw.ellipse(screen,YELLOW,[465,215,60,70])#LLEYE
pygame.draw.polygon(screen,YELLOW,[[455,250],[470,230],[470,270]])#LEYE
pygame.draw.polygon(screen,YELLOW,[[530,280],[518,228],[505,280]])#LLLEYE
pygame.draw.polygon(screen,LBLACK,[[430,85],[527,158],[430,250]])#LEAR
pygame.draw.polygon(screen,LBLACK,[[385,250],[455,220],[455,330]])#LFUR
#NOSE
pygame.draw.polygon(screen,PAWS,[[530,280],[570,280],[550,220]])#NOSE DETAIL
pygame.draw.polygon(screen,NOSE,[[530,280],[570,280],[550,290]])#NOSE
#CAT
pygame.draw.ellipse(screen,BLACK,[470,220,50,60])#EYE
pygame.draw.ellipse(screen,YELLOW,[585,215,60,70])#REYE
pygame.draw.polygon(screen,YELLOW,[[570,280],[592,228],[600,280]])#REYE
pygame.draw.polygon(screen,LBLACK,[[655,220],[730,250],[645,330]])#RFUR
pygame.draw.polygon(screen,YELLOW,[[655,250],[628,218],[628,280]])#REYE
pygame.draw.ellipse(screen,BLACK,[589,220,50,60])#EYE
pygame.draw.polygon(screen,LBLACK,[[580,158],[647,85],[675,250]])#REAR
pygame.draw.circle(screen,FLAME,(552,65),10)#FLAME
pygame.draw.polygon(screen,FLAME,[[560,68],[560,45],[548,65]])#FLAME
#GRASS
pygame.draw.rect(screen,SHGRASS,[0,550,1100,700])#SHGRASS
pygame.draw.rect(screen,GRASS,[0,680,1100,700])#GRASS

#PUMPKIN
pygame.draw.ellipse(screen,DORANGE,[200,310,415,420])#LDORANGE
pygame.draw.ellipse(screen,DORANGE,[500,310,415,420])#RDORANGE
pygame.draw.ellipse(screen,SHORANGE,[425,320,415,430])#RSHORANGE
pygame.draw.ellipse(screen,SHORANGE,[280,320,415,430])#LSHORANGE
pygame.draw.ellipse(screen,ORANGE,[350,300,415,450])#PUMPKIN
#PUMPKIN FACE
pygame.draw.polygon(screen,LBLACK,[[430,400],[360,500],[500,500]])#LEYE
pygame.draw.polygon(screen,LBLACK,[[670,400],[600,500],[740,500]])#REYE
pygame.draw.polygon(screen,LBLACK,[[430,530],[360,550],[500,680]])#MOUTH
pygame.draw.polygon(screen,LBLACK,[[500,680],[550,530],[545,530],[485,660]])#MOUTH
pygame.draw.polygon(screen,LBLACK,[[670,530],[600,680],[740,550]])#MOUTH
pygame.draw.polygon(screen,LBLACK,[[600,680],[550,530],[555,530],[615,660]])#MOUTH
#PAWS
pygame.draw.circle(screen,PAWS,(455,320),40)#LPAW
pygame.draw.circle(screen,PAWS,(655,320),40)#RPAW
#GRASS
pygame.draw.rect(screen,GRASS,[0,720,1100,700])#GRASS
#DISPLAY
pygame.display.update()

x=60
x2=40
x3=70

for i in range(1,50):
    pygame.draw.polygon(screen,SHGRASS,[[x,690],[x2,790],[x3,790]])
    x=x+50
    x2=x2+50
    x3=x3+50
pygame.display.update()


#END
while true:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

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
def VW(a,b,c):
    pygame.draw.circle(screen,c,(a,b),25)#Outer Symbol Outline
    pygame.draw.circle(screen,white,(a,b),21,2)#Inner Symbol Outline
    pygame.draw.rect(screen,white,[a-2.5,b,5,12],4)
    pygame.draw.rect(screen,white,[a-2.5,b,5,-10],4)
    pygame.draw.rect(screen,white,[a-2.5,b-2.5,15,5],4)
    pygame.draw.rect(screen,white,[a-2.5,b-2.5,-9,5],4)
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
    ################################Questions
    while question==3:
        q1=input('''Under what constitution act in what year was the
responsiblilty of healthcare transferred to provincial and
territorial governments
A) 1898
B) 1900
C) 1867
D) 1850
Please type the year you think it is.
=''')
        if q1=='1867':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==7:
        q2=input('''When was Medicare created in Saskatchewan
A) 1960
B) 1962
C) 1989
D) 1961
Please type the year you think it is.
=''')
        if q2=='1962':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==11:
        q3=input('''In what year did N.B adapt
Medicare from Saskatchewan for itself?
A) 1971
B) 1962
C) 1970
D) 1959
Please type the year you think it is.
=''')
        if q3=='1971':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
    while question==15:
        q4=input('''What is the reason for a
walk-in clinic
A) Over-flow from the hospital
B) To help patients(1 in 5 Canadians) who do not
have a family doctor.
C) To help patients who do not have a big
emergency but want help.
D) A doctor's side hustle place.
Please type A, B, C, D for your answer
=''')
        if q4=='C' or 'c':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)

    while question==19:
        q5=input('''Which medical services are insured by Medicare in New Brunswick
A) Over the counter medication
B) Dental services
C) Vision care
D) Hospital and Doctor services
Please type A, B, C, D for your answer.
=''')
        if q5=='D' or 'd':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==23:
        q6=input('''Who is Canada's Minister of Health?
A) Justin Trudeau
B) The Honorable Mark Holland
C) Dorothy Megals
D) The Honorable Shelia
Please type A, B, C, D for your answer
=''')
        if q6=='b' or 'B':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==27:
        q7=input('''Has the government always funded the Hospitals?
A) Yes
B) No
C) Not always
D) I do not know
Please type A, B, C, D for your answer
=''')
        if q7=='C' or 'c' or 'B' or 'b':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==31:
        q8=input('''What is the difference between Health Canada and
Public Health Agency of Canada?
A) Health Canada is for education and the PHAC is for bettering public medication.
B) Health Canada is for bettering medication the PHAC is for dispersing medication 
C) Health Canada is for health policy and regulations and PHAC is for public disease prevention.
D) Health Canada is the boss of PHAC which is for the healthcare for the citizens.
Please type A, B, C, D for your answer
=''')
        if q8=='C' or 'c':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==35:
        q9=input('''What shared-characteristics do the Federal and Provincial
Governments have in hte healthcare system
A) Regulations
B) Funding
C) Delivery
D) All of the above
Please type A, B, C, D for your answer
=''')
        if q9=='D' or 'd':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==39:
        q10=input('''Who is the Health Minister for New Brunswick
A) Blaine Higgs
B) Justin Trudeau
C) Shellia Fenwick
D) Bruce Fitch
Please type A, B, C, D for your answer
=''')
        if q10=='D' or 'd':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==43:
        q11=input('''What is the Tele-Care Number (811) for?
A) The tele-care number is a health advice and information line
B) The tele-care number is a informational line on the wait-times at local hospitals
C) The tele-care number is a health advice line on common flu's
D) The tele-care number is a fake thing
Please type A, B, C, D for your answer
=''')
        if q11=='A' or 'a':
            score=score+150
        else:
            score=score-50
        question=question+1
        restart()
        time.sleep(4)
    while question==47:
        q12=input('''How long can you be out of New Brunswick without
losing Medicare coverage.
A) 1 Month
B) 1 Year
C) 212 Days
D) 6 Motnhs 
Please type A, B, C, D for your answer
=''')
        if q12=='C' or 'c':
            score=score+200
        else:
            score=score-100
        question=question+1
        restart()
        time.sleep(4)
    while question==52:
        q13=input('''Does it cost, in N.B, to transpost you to a hospital
in an emergency situation?
A) No
B) Yes, at a cost of $130
C) Yes, at a cost of $250
D) Yes, at a cost of $50
Please type A, B, C, D for your answer
=''')
        if q13=='B' or 'b':
            score=score+200
        else:
            score=score-100
        question=question+1
        restart()
        time.sleep(4)
    while question==56:
        q14=input('''What is the average amount of time it
takes for an ambulance to arrive at a scene in a town or city
in N.B
A) 15 minutes or less
B) 10 minutes or less
C) 9 minutes or less
D) 5 minutes or less
Please type A, B, C, D for your answer
=''')
        if q14=='C' or 'c':
            score=score+200
        else:
            score=score-100
        question=question+1
        restart()
        time.sleep(4)
    while question==60:
        q15=input('''How is the healthcare system primarly funded
in Canada?
A) Private insurance premiums
B) Government taxes
C) Patient money 
D) Donations and grants
Please type A, B, C, D for your answer
=''')
        if q15=='B' or 'b':
            score=score+200
        else:
            score=score-100
        question=question+1
        restart()
        time.sleep(4)
    
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
            if math.hypot((xu-gx),(yu-gy))<45:
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
            if math.hypot((xu-g1x),(yu-g1y))<45:
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
    elif math.hypot((x1-xu),(y1-yu))<45:
        hearts=hearts-1
        heartt=True
        y1=-15
    elif math.hypot((x2-xu),(y2-yu))<45:
        hearts=hearts-1
        heartt=True
        y2=-15
    elif math.hypot((x3-xu),(y3-yu))<45:
        hearts=hearts-1
        heartt=True
        y3=-15
    elif math.hypot((x4-xu),(y4-yu))<45:
        hearts=hearts-1
        heartt=True
        y4=-15
    if math.hypot((x5-xu),(y5-yu))<45:
        hearts=hearts-1
        heartt=True
        y5=-15
    if math.hypot((x6-xu),(y6-yu))<45:
        hearts=hearts-1
        heartt=True
        y6=-15
    if math.hypot((x7-xu),(y7-yu))<45:
        hearts=hearts-1
        heartt=True
        y7=-15
    if math.hypot((x8-xu),(y8-yu))<45:
        hearts=hearts-1
        heartt=True
        y8=-15
    if math.hypot((x9-xu),(y9-yu))<45:
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




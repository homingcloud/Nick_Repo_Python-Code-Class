import sys
def redo():
    global heart,score,times,ans,ans1,ans2,ans3,ans4,scene
    if heart==0:
        print('Sorry you answered too many questions incorrectly\nIf you wish to restart press r or restart\nOr if you wish to quit type q or quit')
        restart1=input('=')
        if restart1.lower()=='restart' or restart1.lower()=='r':
            heart=3
            score,times=0,0
            ans=[]
            ans1=[]
            ans2=[]
            ans3=[]
            ans4=[]
            scene=0
        elif restart1.lower()=='quit' or restart1.lower()=='q':
            print('Okay you have choosen to quit \nGoodbye')
            sys.exit()

name=input('Hello my name is Nic Robot, what is your name?\n=')
print('Well hello',name,'for this program I will provide a hint towards which you\nwill need to guess the word related to it\nfor every correct word you get 100 points if it is a tier 1 word and 200 for a tier 2 word\nand 300 for a tier 3 word.')
print('')

heart=3
score,times,word=0,0,0
scene=1

ans=[]
ans1=[]
ans2=[]
ans3=[]
ans4=[]

tier1=['brakes','engine','battery','exhaust','spark plug','torque','spark plugs','file','air compressor','multimeter','oil drain pan','rachet','tires','flashlight','tire pressure guage','wrench set','gloves','wheels','brake','screwdrivers','screwdriver','pliers','electrical','electricity','electric','thrust','kinetic','linear','hammer']
tier2=['transmission','oil pump','timing belt','radiator','intertia','alternator','fuel pump','differential','muffler','impact gun','impact','tire balancer','pry bar','stud extractor','turbocharger','mechanical','suspension','tension','compression','thermal','rotational','wrench']
tier3=['differential','harmonic','throttle body','power steering pump','shear','brake bleeder kit','oil filter wrench','tranmission jack','welding machine','cylinder compression tester','obd scanner','obd scanner tool','diagnostic scanner','aligner','potential','valve','valves','hydraulic lift','torque wrench','fuel injector','oscillatory','regenerative','chemical','caliper']

print('')
print('For your hint towards a word here it is.')
print('There are three possibile answers to the question each being more sophisticated\nearning you more points if you get the more sophisticated answer.')
print('')

while len(ans)+len(ans1)+len(ans2)+len(ans3)+len(ans4)!=15:
    if word==1:
        print('')
        print('Good job you got through your first round of questions\nNow answer the questions with different answers until you get three answer correct\nMeaning three rounds if you get them all perfect')
        word+=1
    if scene==1:
        if times>0:
            print('')
            print('Round#',times+1,'now begins')
        print('Question#1: What are common types of mechanical components in vehicles?')
        if len(ans)<3:
            if len(ans)>0:
                print('You have so far guessed the words',', '.join(ans))
            answer=input('=')
            answer=answer.lower()
            if answer in tier1:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+100
                ans.append(answer)
            elif answer in tier2: 
                if heart<3:
                    heart=heart+1
                else:
                    score=score+200
                ans.append(answer)
            elif answer in tier3:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+300
                ans.append(answer)
            else:
                heart=heart-1
                print('Sorry that is not in the word bank,you have',heart,'hearts left')
                print('')
                redo()
            scene+=1
        print('Your score so far is',score)
        print('')
    elif scene==2:
        if len(ans1)<3:
            print('Question#2: What are types of mechanical forces used in a cars systems?')
            if len(ans1)>0:
                print('You have so far guessed the words',', '.join(ans1)) 
            answer1=input('=')
            answer1=answer1.lower()
            if answer1 in tier1:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+100
                ans1.append(answer1)
            elif answer1 in tier2: 
                if heart<3:
                    heart=heart+1
                else:
                    score=score+200
                ans1.append(answer1)
            elif answer1 in tier3:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+300
                ans1.append(answer1)
            else:
                heart=heart-1
                print('Sorry that is not in the word bank,you have',heart,'hearts left')
                print('')
                redo()
            scene+=1
        print('Your score so far is',score)
        print('')
    elif scene==3:
        if len(ans2)<3:
            print('Question#3: What are types of mechanical energies used in a cars system?\nYou do not need to put energy in the response')
            if len(ans2)>0:
                print('You have so far guessed the words',', '.join(ans2))
            answer2=input('=')
            answer2=answer2.lower()
            if answer2.lower() in tier1:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+100
                ans2.append(answer2)
            elif answer2 in tier2: 
                if heart<3:
                    heart=heart+1
                else:
                    score=score+200
                ans2.append(answer2)
            elif answer2 in tier3:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+300
                ans2.append(answer2)
            else:
                heart=heart-1
                print('Sorry that is not in the word bank,you have',heart,'hearts left')
                print('')
                redo()
            scene+=1
        print('Your score so far is',score)
        print('')
    elif scene==4:
        if len(ans3)<3:
            print('Question#4: What are some types of mechanical motions used in a cars system?')
            if len(ans3)>0:
                print('You have so far guessed the words',', '.join(ans3))
            answer3=input('=')
            answer3=answer3.lower()
            if answer3 in tier1:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+100
                ans3.append(answer3)
            elif answer3 in tier2: 
                if heart<3:
                    heart=heart+1
                else:
                    score=score+200
                ans3.append(answer3)
            elif answer3 in tier3:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+300
                ans3.append(answer3)
            else:
                heart=heart-1
                print('Sorry that is not in the word bank,you have',heart,'hearts left')
                print('')
                redo()
            scene+=1
        print('Your score so far is',score)
        print('')
    elif scene==5:
        if len(ans4)<3:
            print('Question#5: What are some mechanical tools used by mechanics?')
            if len(ans4)>0:
                print('You have so far guessed the words',', '.join(ans4))
            answer4=input('=')
            answer4=answer4.lower()
            if answer4 in tier1:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+100
                ans4.append(answer4)
            elif answer4 in tier2: 
                if heart<3:
                    heart=heart+1
                else:
                    score=score+200
                ans4.append(answer4)
            elif answer4 in tier3:
                if heart<3:
                    heart=heart+1
                else:
                    score=score+300
                ans4.append(answer4)
            else:
                heart=heart-1
                print('Sorry that is not in the word bank,you have',heart,'hearts left')
                print('')
                redo()
        print('Your score so far is',score)
        print('')
        times=times+1
        word=word+1
        scene=1
print('Good job,',name,'\n you succesfully answered the questions')
print('Your final socre is',score)
sys.exit()
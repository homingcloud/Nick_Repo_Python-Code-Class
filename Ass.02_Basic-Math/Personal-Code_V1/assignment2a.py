import sys
initialcontact,loop1=1,1
#Ask user for name 
name=input('Hello, my name is Nicksys, what is yours\n:')
print('\nHello',name,'for this program I will calculate two numbers you give me')
goinitial=input('If you chooose to continue please enter continue in the line below\n:')
goinitial=goinitial.lower()
if goinitial!='continue':
    while loop1==1:
        if initialcontact==1:
            print('Sorry that is an invalid input, please try again.\nOr type stop to exit')
            goinitial=input('If you chooose to continue please enter continue in the line below\n:')
            goinitial=goinitial.lower()
            if goinitial=='continue':
                loop1=0
            elif goinitial=='stop':
                exit()
            else:
                loop1=1
                initialcontact=0
        elif initialcontact==0:
            print('Sorry that is an invalid input, please try again.\nOr type stop to exit')
            goinitial=input('If you chooose to continue please enter continue in the line below\n:')
            goinitial=goinitial.lower()
            if goinitial=='continue':
                loop1=0
            elif goinitial=='stop':
                exit()
            else:
                loop1=1
print('\nOkay thank you for choosing to continue with my program, have a great time\n')

num1=input('Please input the first number:')
num2=input('Please input the second number:')


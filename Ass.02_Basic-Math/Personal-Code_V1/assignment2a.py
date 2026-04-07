import sys
initialcontact1,initialcontact2,initialcontact3,loop1,loop2,loop3=1,1,1,1,1,1
#Ask user for name 
name=input('Hello, my name is Nicksys, what is yours\n:')
print('\nHello',name,'for this program I will calculate two numbers you give me')
#Ask user to continue or not
goinitial=input('If you chooose to continue please enter continue in the line below\n:')
#Checking if goinitial request is to continue or an eror
#Lowering for simplicity 
goinitial=goinitial.lower() 
#Making error loop if goinitial is not continue exactly
if goinitial!='continue':
    while loop1==1:
        #Initial message single loop NEED TO FIX AS DOUBLE GOINITIAL='CONTINUE' BLOCKS ARE REDUNDANT, WILL FIX LATER
        if initialcontact1==1:
            print('Sorry that is an invalid input, please try again.\nOr type stop to exit')
            goinitial=input('If you chooose to continue please enter continue in the line below\n:')
            goinitial=goinitial.lower()
            #If goinitial request is not continue keep on looping
            if goinitial=='continue':
                loop1=0
            #Option to quit if goinitial request is stop
            elif goinitial=='stop':
                print('Thank you for choosing this program, have a great day')
                exit()
            else:
            #Continue to loop if it does not work and cutoff initialcontact loop 
                loop1=1
                initialcontac1=0
        elif initialcontac1==0:
            print('Sorry that is an invalid input, please try again.')
            goinitial=input('If you chooose to continue please enter continue in the line below or type stop to stop\n:')
            goinitial=goinitial.lower()
            if goinitial=='continue':
                loop1=0
            elif goinitial=='stop':
                print('Thank you for choosing this program, have a great day')
                exit()
            else:
                loop1=1
print('\nOkay thank you for choosing to continue with my program, have a great time\n')
#Ask user for inputs
num1=input('Please input the first number:')
num2=input('Please input the second number:')
def basemath(num1,num2):
    #Sum Code
    sum1=num1+num2
    #Product Code
    pro1=num1*num2
    #Difference Code
    diff1=num1-num2 
    return sum1,pro1,diff1
try:
    num1/num2
except: 
    try:
        num2/num1
    except:
        diffquo='none'
        print('Sorry the values inputed are not viable for the quotient')
        goquo=input('If you would like to re-input the quotient values only please enter "quotient"\nOr if you would like to enter new values for all processes please enter "all"\n=')
        goquo=goquo.lower()
        if goquo=='quotient':
            numquo1=input('Please input the first number for the quotient:')
            numquo2=input('Please input the second number for the quotient:')
            try:
                numquo1/numquo2
            except:
                print('Sorry that is again an invalid value as determined by the division')

        elif goquo=='all':
            numall1=input('Please input the first number for the redo:')
            numall2=input('Please input the second number for the redo:')
        else:
            while loop3==1:
                if initialcontact3==1:
                    print('Sorry that is an invalid input for this question, please try again or type stop to exit')
                    goquo=input('If you would like to re-input the quotient values only please enter "quotient"\nOr if you would like to enter new values for all processes please enter "all"\n=')
                    goquo=goquo.lower()
                    if goquo=='quotient':
                        print('sss')
                    elif goquo=='all':
                        print('sss')
                    elif goquo=='stop':
                        print('Thank you for choosing this program, have a great day')
                        exit()
                    else:
                        loop3=1
                        initialcontact3=0
                elif initialcontact3==0:
                    print('Sorry that is an invalid input for this question, please try again')
                    goquo=input('If you would like to re-input the quotient values only please enter "quotient"\nOr if you would like to enter new values for all processes please enter "all"\n=')
                    goquo=goquo.lower()
                    if goquo=='quotient':
                        print('sss')
                    elif goquo=='all':
                        print('sss')
                    else:
                        loop3=1
                        


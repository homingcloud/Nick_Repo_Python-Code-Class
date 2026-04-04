import random

 

count = 0
score = 0

 

def scoreadd():
    global score
    global count
    count = count + 1
    score = count * 5
    return print('Your score is', score)

 

def correct():
    print('That\'s correct! 5 points to your score!')
    scoreadd()

 

def incorrect():
    print('You are incorrect :( Good luck next time!')

 

def q1():
    print('What is the capital of Russia?')
    print('''1. Samara
2. Moscow
3. St. Petersburg
4. Novosibirsk''')
    answer = int(input('What is your answer?'))
    if answer == 2:
        correct()
    elif answer != 2:
        incorrect()

 

def q2():
    print('What is the capital of Sweden?')
    print('''1. Stockholm
2. Gothenburg
3. Borgholm
4. Djursholm''')
    answer = int(input('What is your answer?'))
    if answer == 1:
        correct()
    elif answer != 1:
        incorrect()

 

def q3():
    print('what is the captial of Greece?')
    print('''1. Thessaloniki
2. Patras
3. Heraklion
4. Athens''')
    answer=int(input('what is your answer?'))
    if answer==4:
        correct()
    elif answer!=4:
        incorrect()
def q4():
    print('what is the captial of Israel?')
    print('''1.Beer-Sheva
2. Jerusalem
3. Tel-Aviv
4. Arad''')
    answer=int(input('what is your answer?'))
    if answer==3:
        correct()
    elif answer!=3:
        incorrect()
def q5():
    print('what is the captial of the Czech Republic?')
    print('''1. Brno
2. Ostrava
3. Liberec
4. Prague''')
    answer=int(input('what is your answer?'))
    if answer==4:
        correct()
    elif answer!=4:
        incorrect()
def q6():
    print('what is the captial of Latvia?')
    print('''1. Riga
2. Jelgava
3. Daugavplis
4. Ventspits''')
    answer=int(input('what is your answer?'))
    if answer==1:
        correct()
    elif answer !=1:
        incorrect()
def q7():
    print('what is the captial of South Korea?')
    print('''1. Andong
2. Seoul
3. Gwangju
4. Paju''')
    answer=int(input('what is your answer?'))
    if answer==2:
        correct()
    elif answer !=2:
        incorrect() 
def q8():
    print('what is the captial of Finland?')
    print('''1. Huittinen
2. Espoo
3. Helsinki
4. Nokia''')
    answer=int(input('what is your answer?'))
    if answer==3:
        correct()
    elif answer!=3:
        incorrect()
def q9():
    print('what is the captial of Syria?')
    print('''1. Aleppo
2. Hama
3. Latakia
4. Damascus''')
    answer=int(input('what is your answer?'))
    if answer==4:
        correct()
    elif answer!=4:
        incorrect()
def q10():
    print('what is the captial of Egypt?')
    print('''1. Alexandria
2. Cairo
3. Giza
4. Suez''')
    answer=int(input('what is your answer?'))
    if answer==2:
        correct()
    elif answer !=2:
        incorrect()


print('Welcome to this geographical quiz!')
print(r"""
            _,\?dZkMHF&$*q#b..
          .//9MMMMMMM?:'HM\\"`-''`..
       ..`  :MMMMMMMMMMHMMMMH?_    `-\
     .     .dMMMMMMMMMMMMMM'"'"       `\.
    .      |MMMMMMMMMMMMMR              \\
   -        T9MMMMMHH##M"                `?
  :          (9MMM'    !':.               &k
 .:            HMM\_?p "":-b\.            `ML
-                "'"H&#,       :           |M|
:                     ?\,\dMH#b#.           9b
:                        |MMMMMMM##,        `*
:                   .   +MMMMMMMMMMMo_       -
:                       HMMMMMMMMMMMMMM#,    :
:                        9MMMMMMMMMMMMMH'    .
: .                       *HMMMMMMMMMMP     .'
 :                          MMMMMMMMMH'     .
  -                        :MMMMMMM'`      .
  `.                       9MMMMM*'       -
    -.                    {MMM#'         :
      -                  |MM"          .'
       `.                &M'..  .   ..'
          ' .             ._     .-
              '-. -voboo#&:,-.-`
              """)
#Please print your answers numerically and not the name of the city''')
 

# Create a list of question functions
question_functions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

 

# Shuffle the list of questions
random.shuffle(question_functions)

 

# Ask questions in the randomized order
for question_function in question_functions:
    question_function()

#make the quiz a bit longer. lets make an optional second part.
#before that we need to make the functions for this line of questions
def q11():
    print('Buenos Aires is the capital of which country?')
    print('''1. Argentina
2. Chile
3. Brazil
4. Ecuador''')
    answer=int(input('what is your answer?'))
    if answer==1:
        correct()
    elif answer !=1:
        incorrect()
def q12():
    print('Copenhagen is the capital of which country?')
    print('''1. Sweden
2. Finland
3. Denmark
4. England''')
    answer=int(input('what is your answer?'))
    if answer==3:
        correct()
    elif answer !=3:
        incorrect()
def q13():
    print('Dublin is the capital of which country?')
    print('''1. Ireland
2. Wales
3. United Kingdom
4. Australia''')
    answer=int(input('what is your answer?'))
    if answer==1:
        correct()
    elif answer !=1:
        incorrect()
def q14():
    print('Madrid is the capital of which country?')
    print('''1. Italy
2. Spain
3. Mexico
4. France''')
    answer=int(input('what is your answer?'))
    if answer==2:
        correct()
    elif answer !=2:
        incorrect()
def q15():
    print('Canberra is the capital of which country?')
    print('''1. Isle Of Man
2. Jamaica
3. USA
4. Australia''')
    answer=int(input('what is your answer?'))
    if answer==4:
        correct()
    elif answer !=4:
        incorrect()
def q16():
    print('Berlin is the capital of which country?')
    print('''1. Netherlands
2. Switzerland
3. Germany
4. Poland''')
    answer=int(input('what is your answer?'))
    if answer==3:
        correct()
    elif answer !=3:
        incorrect()
def q17():
    print('Yerevan is the capital of which country?')
    print('''1. Argentina
2. Armenia
3. Georgia
4. Ireland''')
    answer=int(input('what is your answer?'))
    if answer==2:
        correct()
    elif answer !=2:
        incorrect()
def q18():
    print('Amsterdam is the capital of which country?')
    print('''1. Netherlands
2. Russia
3. New Zealand
4. Pakistan''')
    answer=int(input('what is your answer?'))
    if answer==1:
        correct()
    elif answer !=1:
        incorrect()
def q19():
    print('Taipei is the capital of which country?')
    print('''1. Taiwan
2. Japan
3. Hong Kong
4. China''')
    answer=int(input('what is your answer?'))
    if answer==1:
        correct()
    elif answer !=1:
        incorrect()
def q20():
    print('Ankara is the capital of which country?')
    print('''1. Vietnam
2. UAE
3. Iran
4. Turkey''')
    answer=int(input('what is your answer?'))
    if answer==4:
        correct()
    elif answer !=4:
        incorrect()
repeat=int(input('would you like to switch it up a little? (1=yes)'))
while repeat==1:
    # Create a list of question functions
    question_functions = [q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]

 # Shuffle the list of questions
    random.shuffle(question_functions)

    for question_function in question_functions:



        question_function()
    repeat=0


if score==100:
    print('a', score, '! good job geo wiz! you got all the answers right!')
if score >=90 and score <=99:
    print('a', score, '! very good! you got most of the questions right!')
if score >=80 and score <=89:
    print('a', score, '! not bad! you\'re quite alright at geography')
if score >=70 and score <=79:
    print('a', score, '! you\'re up there! more than half is still a win!')
if score >=60 and score <=69:
    print('a', score, '! keep learning! you\'ll be up there soon!')
if score ==50:
    print('a', score, '! you got more half the questions right, not too bad.')
if score <50:
    print('a', score, '! less than half just means you\'re learning. Dont worry, you\'ll get there eventually!')


print('Hello my name is Nicksys, for this program I have for you a Caesear Cipher machine ')
name=input('First of all what is you name?\n=')
wordt=input('Please type in a word that you would like to put through the Caesar Cipher machine\n=')
print('You can either shift each letter backwards by typing ')
shift=int(input('How many times would you like to shift the letter\n='))
while True:
    x=0
    y=0
    letters=[]
    for  letter in wordt:
        letters.append(letter)
        y=y+1
    if shift>0:
        for i in range(y):
            number=ord(letters[x])
            if number==32:
                j=letters.pop(x)
                myletter=chr(number)
                letters.insert(x,myletter)
            else:
                number+=shift
                if number==123:
                    number=97
                j=letters.pop(x)
                myletter=chr(number)
                letters.insert(x,myletter)
            x+=1
        print(''.join(letters))
    elif shift<0:
        for i in range(y):
            number=ord(letters[x])
            if number==32:
                j=letters.pop(x)
                myletter=chr(number)
                letters.insert(x,myletter)
            else:    
                number-=shift
                if number==96:
                    number=122
                j=letters.pop(x)
                myletter=chr(number)
                letters.insert(x,myletter)
            x+=1
        print(''.join(letters))
    else:
        print('Sorry that is an invalid number of shifts\nPlease retype the number of shifts correctly')
        print('')
        wordt=input('Please type in a word that you would like to put through the Caesar Cipher machine\n=')
        print('You can either shift each letter backwards by typing ')
        shift=int(input('How many times would you like to shift the letter\n='))
    go=input('Do you wish to redo the program and redo the Caesar Cipher machine?\nType y for yes or n for no\n=')
    if go.lower()=='y' or go.lower()=='yes':
        wordt=input('Please type in a word that you would like to put through the Caesar Cipher machine\n=')
        print('You can either shift each letter backwards by typing ')
        shift=int(input('How many times would you like to shift the letter\n='))
    else:
        False

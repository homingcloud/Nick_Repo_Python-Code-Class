times=0
name=input('Hello my name is Nic Robot, what is your name?\n=')
print('Well hello',name,'for this program you will enter words\nand I will order them alphabetically')
print('')
times=int(input('How many words do you want to enter for this program?\n='))
wordlist=[]

word0=input('Input your first word here\n=')
wordlist.append(word0)
for i in range(times-2):
    word1=input('Input your next word here\n=')
    wordlist.append(word1)
word2=input('Input your last word here\n=')
wordlist.append(word2)

print('Here are the words in order aplhabetically')
print('')
sortedwords=sorted(wordlist)
print(', '.join(sortedwords))
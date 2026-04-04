times = 0
name = input('Hello, my name is Nic Robot. What is your name?\n=')
print('Well hello', name, 'for this program you will enter words\nand I will order them alphabetically.')
print('')
times = int(input('How many words do you want to enter for this program?\n='))
wordlist = []

# Collecting words from the user
for i in range(times):
    word = input('Input your word number {i + 1} here\n=')
    wordlist.append(word)

# Sorting the word list
sorted_words = sorted(wordlist)
print('Here are the words in order alphabetically:')
print(', '.join(sorted_words))  # Printing words in one line

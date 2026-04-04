x=0
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(', '.join(alpha))
print('')
for i in range(26):
    number=ord(alpha[x])
    number+=1
    if number==123:
        number=97
    j=alpha.pop(x)
    myletter=chr(number)
    alpha.insert(x,myletter)
    x+=1
print(', '.join(alpha))
print('')
x=0
for i in range(26):
    number=ord(alpha1[x])
    number-=1
    if number==96:
        number=122
    j=alpha1.pop(x)
    myletter=chr(number)
    alpha1.insert(x,myletter)
    x+=1
print(', '.join(alpha1))


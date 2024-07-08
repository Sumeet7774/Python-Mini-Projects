# Word game using shuffle

import random as r

word = input('Enter Animal Quiz : ')
length = len(word)

idx = [i for i in range(0,length)]
r.shuffle(idx)
#print(idx)


shuf = ''
for i in idx:
    shuf += word[i]
print('')
print('Crack this word: ',shuf)

ans = input('Enter your answer : ')
if ans.upper() == word.upper():     
    print('Your answer is correct')
else:
    print('Wrong answer')    













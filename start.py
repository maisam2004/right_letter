import string,random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list=list('?'*len(the_word))
print(clue_list)
whole_letters =string.ascii_letters
#print(whole_letters)

heartlist=list("\u2764\ufe0f"*9)

word = 'mirkos'
clu = ['?','?','?','?','?','?']
while True:
    guess= input('guess you letter ')
    if word.count(guess) > 0:
        ind = word.index(guess)
        clu[ind]=guess
        #for i,l in enumerate(word):
            #ln= word.count(l)
           # for i in range(ln):
    elif word.count(guess) == 0:
        print('you lost one of your heart')
        heartlist.pop()
    if '?' not in clu:
        print('well done',''.join(clu))
        break
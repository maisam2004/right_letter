import string
import random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list=list('?'*len(the_word))
cu=list('?'*len(the_word))

whole_letters =string.ascii_letters
#print(whole_letters)

heartlist=list("\u2764"*9)

all_guesses =''

while heartlist :
    guess= input('guess you letter ') #request letter
    if guess not in whole_letters:
        guess= input('PLEASE ENTER ONLY LETTERS ') #request letter if first try did not enter nubmer
    all_guesses += guess
    if guess in the_word and guess not in clue_list:
        
        for i,l in enumerate(the_word): # loop to remove any doble letters
            if l == guess:
                clue_list[i] = guess

        print(''.join(clue_list),'<< this is your guess so far ',f'you have {len(heartlist)} lives left',sep=' ')
        
    else:
        print('you lost one of your heart')
        heartlist.pop() #remove one heart
        print(heartlist,f'only this {len(heartlist)} lives left')
    if '?' not in clue_list:
        print('well done the word was > ',''.join(clue_list),''.join(set(heartlist)))
        break

print(f'the word was>>{the_word}')
print('all of your guesses >>','-'.join(list(all_guesses)))
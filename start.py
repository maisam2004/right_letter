import string,random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list=list('?'*len(the_word))
print(clue_list)
whole_letters =string.ascii_letters
#print(whole_letters)

heartlist=list("\u2764"*9)



while heartlist :
    guess= input('guess you letter ') #request letter
    if guess not in whole_letters:
        guess= input('PLEASE ENTER ONLY LETTERS ') #request letter if first try did not enter nubmer
    if guess in the_word and guess not in clue_list:
        num_lettrs= the_word.count(guess) #find the number of times letters in word
        new_word = the_word #copy of main word
        for _ in range(num_lettrs): # loop to remove any doble letters
            ind = new_word.index(guess)
            
            clue_list[ind]=guess
            new_word = new_word.replace(new_word[ind],'_',1)

        print(''.join(clue_list),'<< this is your guess so far ',f'you have {len(heartlist)} lives left',sep=' ')
        
    else:
        print('you lost one of your heart')
        heartlist.pop() #remove one heart
        print(heartlist,f'only this {len(heartlist)} lives left')
    if '?' not in clue_list:
        print('well done the word was > ',''.join(clue_list),''.join(set(heartlist)))
        break

print(f'the word was>>{the_word}')
import string,random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list=list('?'*len(the_word))
print(clue_list)
whole_letters =string.ascii_letters
#print(whole_letters)

heartlist=list("\u2764"*9)

word = 'mirros'
clu = ['?','?','?','?','?','?']
while heartlist :
    guess= input('guess you letter ')
    if guess not in whole_letters:
        guess= input('PLEASE ENTER ONLY LETTERS ')
    if guess in word and guess not in clu:
        num_lettrs= word.count(guess)
        for _ in range(num_lettrs):
            ind = word.index(guess)
            print(ind,'this index of letter')
            clu[ind]=guess
            word = word.replace(word[ind],'_',1)

        print(''.join(clu),'<< this is your guess so far ',f'you have {len(heartlist)} lives left',sep=' ')
        
    else:
        print('you lost one of your heart')
        heartlist.pop()
        print(heartlist,f'only this {len(heartlist)} lives left')
    if '?' not in clu:
        print('well done',''.join(clu))
        break
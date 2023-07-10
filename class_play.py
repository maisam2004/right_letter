import string
import random
from wonderwords import RandomWord

class let_guess:
    def __init__(self) :
        self.word_generator = RandomWord()
        self.the_word =self.word_generator.word()
        self.whole_letters = string.ascii_letters
        self.clue_list = ['?']*len(self.the_word)
        self.heartlist = list("\u2764" * 9)
        self.all_guesses = ''

    def play(self):
        while self.heartlist :
            guess= input('guess you letter ') #request letter
            if guess not in self.whole_letters:
                guess= input('PLEASE ENTER ONLY LETTERS ') #request letter if first try did not enter nubmer
            self.all_guesses += guess
            if guess in self.the_word and guess not in self.clue_list:
                
                for i,l in enumerate(self.the_word): # loop to remove any doble letters
                    if l == guess:
                        self.clue_list[i] = guess

                print(''.join(self.clue_list),'<< this is your guess so far ',f'you have {len(self.heartlist)} lives left',sep=' ')
                
            else:
                print('you lost one of your heart')
                self.heartlist.pop() #remove one heart
                print(self.heartlist,f'only this {len(self.heartlist)} lives left')
                if len(self.heartlist) <1:
                    print(f'the word was>>{self.the_word}')
                    print('all of your guesses >>','-'.join(list(self.all_guesses)))
                    
            if '?' not in self.clue_list:
                print('well done the word was > ',''.join(self.clue_list),''.join(set(self.heartlist)))
                break




if __name__ == '__main__':
    new_game = let_guess()
    new_game.play()
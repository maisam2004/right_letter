import string
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

            guess = self.check_guess(guess)
            self.all_guesses += guess 
            if guess in self.the_word and guess not in self.clue_list:

                self.clue_list=self.righ_loop(guess)
                print(''.join(self.clue_list),'<< this is your guess so far ',f'you have {len(self.heartlist)} lives left',sep=' ')

            else:
                self.loosing()

            if '?' not in self.clue_list:
                self.win()
                break

    def check_guess(self,guess):
        if guess not in self.whole_letters:
            guess= input('PLEASE ENTER ONLY LETTERS ')
            return guess
        return guess
    
    def righ_loop(self,guess):
        for i,l in enumerate(self.the_word): # loop to remove any doble letters
                if l == guess:
                    self.clue_list[i] = guess
        return self.clue_list
    
    def loosing(self):
        self.heartlist.pop() #remove one heart
        print('you lost one of your heart')
        print(self.heartlist,f'only this {len(self.heartlist)} lives left')

        if len(self.heartlist) <1: #check if lost
            self.lost()
    
    def lost(self): #lost game
        print(f'Sory you lost :< the word was>>{self.the_word}')
        print('all of your guesses >>','-'.join(list(self.all_guesses)))

    def win(self):
        print('well done the word was > ',''.join(self.clue_list),''.join(set(self.heartlist)))
       



if __name__ == '__main__':
    new_game = let_guess()
    new_game.play()
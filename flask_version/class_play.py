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
        #self.letter = letter

    def play(self):
        while self.heartlist :
            guess= input('guess you letter ') #request letter
            guess = self.letter
            guess = self.check_guess(guess)
            self.all_guesses += guess 
            if guess in self.the_word and guess not in self.clue_list:

                self.clue_list=self.righ_loop(guess)
                self.short_loos_message()

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
        if len(self.heartlist) < 1:
            message = f'You lost! The word was: {self.the_word}'
            message += f' All of your guesses: {", ".join(self.all_guesses)}'
            return message
        
        self.heartlist.pop() # remove one heart
        message = 'You lost one of your hearts. <i class="fa-solid fa-heart" style="color: #888b91;"></i>'
        message += f' Only {len(self.heartlist)} <i class="fa-solid fa-heart" style="color: #888b91;"></i> left.'
        return message

        if len(self.heartlist) <1: #check if lost
            self.lost()
    
    def lost(self): #lost game
        message=f'Sory you lost :< the word was>>{self.the_word}'
        message+= 'all of your guesses >>','-'.join(list(self.all_guesses))
        return message

    def win(self):
        message=f'well done the word was > ',''.join(self.clue_list),''.join(set(self.heartlist))
        return message
    def short_loos_message(self):
        message = f"{''.join(self.clue_list)}+'<< this is your guess so far ','you have {len(self.heartlist)} lives left'"
        return message 



""" if __name__ == '__main__':
    new_game = let_guess()
    new_game.play() """
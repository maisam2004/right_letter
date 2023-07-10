#'AI generate this


import string
import random
from wonderwords import RandomWord

class HangmanGame:
    def __init__(self):
        self.word_generator = RandomWord()
        self.the_word = self.word_generator.word()
        self.clue_list = ['?'] * len(self.the_word)
        self.heartlist = list("\u2764" * 9)

    def play(self):
        print(self.clue_list)

        while self.heartlist:
            guess = self.get_guess()
            if not self.validate_guess(guess):
                continue

            if guess in self.the_word and guess not in self.clue_list:
                self.update_clue_list(guess)
                print(' '.join(self.clue_list), f'<< This is your guess so far. You have {len(self.heartlist)} lives left.')

            else:
                self.lose_life()
                print(self.heartlist, f'Only {len(self.heartlist)} lives left.')

            if '?' not in self.clue_list:
                self.game_over(True)
                return

        self.game_over(False)

    def get_guess(self):
        return input('Guess a letter: ')

    def validate_guess(self, guess):
        if guess not in string.ascii_letters:
            print('PLEASE ENTER ONLY LETTERS')
            return False
        return True

    def update_clue_list(self, guess):
        for i, letter in enumerate(self.the_word):
            if letter == guess:
                self.clue_list[i] = guess

    def lose_life(self):
        print('You lost one of your lives.')
        self.heartlist.pop()

    def game_over(self, win):
        if win:
            print('Well done! The word was:', ' '.join(self.clue_list))
        else:
            print('You lost! The word was:', self.the_word)

game = HangmanGame()
game.play()

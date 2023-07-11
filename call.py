#'AI generate this


import string
import random
from wonderwords import RandomWord

class HangmanGame:
    def __init__(self):
        ##create attributes 
        self.word_generator = RandomWord()
        self.the_word = self.word_generator.word()
        self.clue_list = ['?'] * len(self.the_word)
        self.heartlist = list("\u2764" * 9)

    def play(self):
        ## do while for input ,while heartlist is True
        while self.heartlist:
            guess = self.get_guess() # get_guess method 
            if not self.validate_guess(guess): # validate methos for in string check
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


"""
The given Python code is an implementation of the Hangman game. Here's a breakdown of the code: 1. The code begins by importing necessary modules: `string`, `random`, and `wonderwords` from the library `RandomWord`. 
2. The `HangmanGame` class is defined, which encapsulates the logic of the game. 
3. In the `__init__` method of `HangmanGame`, the attributes of the game are initialized: - `word_generator` is an instance of the `RandomWord` class from the `wonderwords` library, used to generate a random word. - `the_word` stores the randomly generated word. - `clue_list` is a list that represents the current state of the word, with each letter initially represented by a question mark ('?'). - `heartlist` is a list that represents the number of lives remaining, with each life represented by a heart symbol ('\u2764'). 

4. The `play` method is defined to start the game. It contains the main game loop that continues until the `heartlist` is empty. 

5. Inside the game loop, the `get_guess` method is called to get a user's guess. 


6. The `validate_guess` method is then called to check if the guess is a valid letter. If it is not a letter, an error message is printed and the loop continues with the next iteration. 

7. If the guess is valid, the code checks if the guess is present in the randomly generated word and if it is not already revealed in the `clue_list`. If so, the `update_clue_list` method is called to update the `clue_list` with the correctly guessed letter. 

8. If the guess is not present in the word, the `lose_life` method is called to decrement the remaining lives. 
9. After each guess, the current state of the `clue_list` and the number of remaining lives are printed. 
10. The loop continues until either the `clue_list` no longer contains any question marks ('?'), indicating that the word has been completely guessed, or the `heartlist` is empty, indicating that the player has no more lives remaining. 

11. Finally, the `game_over` method is called to print a message indicating whether the player won or lost and reveal the word. 

12. An instance of the `HangmanGame` class is created, and the `play` method is called to start the game. Note: The code uses the `input` function to get user input from the command line.
"""
import string
import random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list = ['?'] * len(the_word)
print(clue_list)

whole_letters = string.ascii_letters

heartlist = list("\u2764" * 9)

while heartlist:
    guess = input('Guess a letter: ')  # Request a letter
    if guess not in whole_letters:
        guess = input('PLEASE ENTER ONLY LETTERS: ')  # Request a letter if the input is not a letter

    if guess in the_word and guess not in clue_list:
        num_letters = the_word.count(guess)  # Find the number of times the letter appears in the word
        new_word = the_word  # Create a copy of the main word

        for _ in range(num_letters):  # Loop to handle duplicate letters
            ind = new_word.index(guess)
            clue_list[ind] = guess
            new_word = new_word.replace(new_word[ind], '_', 1)

        print(' '.join(clue_list), f'<< This is your guess so far. You have {len(heartlist)} lives left.')

    else:
        print('You lost one of your lives.')
        heartlist.pop()  # Remove one life
        print(heartlist, f'Only {len(heartlist)} lives left.')

    if '?' not in clue_list:
        print('Well done! The word was:', ' '.join(clue_list))
        break

print('The word was:', the_word)

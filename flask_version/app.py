from flask import Flask, redirect, render_template, request
import string
from wonderwords import RandomWord

app = Flask(__name__)
word_generator = RandomWord()
the_word = word_generator.word()

clue_list = ['?'] * len(the_word)
whole_letters = string.ascii_letters
heartlist = list("\u2764" * 9)


@app.route('/', methods=['GET', 'POST'])
def home():
    global the_word, clue_list, heartlist

    if request.method == 'POST':
        guess = request.form['letter']
        if guess not in whole_letters:
            message = 'PLEASE ENTER ONLY LETTERS: '
        else:
            if guess in the_word and guess not in clue_list:
                for i, l in enumerate(the_word):
                    if l == guess:
                        clue_list[i] = guess

                message = ' '.join(clue_list) + f'<< This is your guess so far. You have {len(heartlist)} lives left.'
            else:
                heartlist.pop()
                message = f"You lost one of your lives. Only {len(heartlist)} lives left."

            if '?' not in clue_list:
                message = 'Well done! The word was: ' + ' '.join(clue_list)
    else:
        message = ''

    return render_template("home.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

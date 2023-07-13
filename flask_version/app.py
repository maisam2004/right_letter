from flask import Flask, redirect, render_template, request, session
import string
from wonderwords import RandomWord

app = Flask(__name__)
app.secret_key = 'your-secret-key'

def generate_word():
    word_generator = RandomWord()
    return word_generator.word()

def initialize_game():
    session['the_word'] = generate_word()
    session['clue_list'] = ['?'] * len(session['the_word'])
    session['heartlist'] = list("\u2764" * 9)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'the_word' not in session:
        initialize_game()

    the_word = session['the_word']
    clue_list = session['clue_list']
    heartlist = session['heartlist']

    if request.method == 'POST':
        guess = request.form['letter']
        if guess not in string.ascii_letters:
            message = 'PLEASE ENTER ONLY LETTERS: '
        else:
            if guess in the_word and guess not in clue_list:
                for i, l in enumerate(the_word):
                    if l == guess:
                        clue_list[i] = guess

                message = ' '.join(clue_list) + f' << This is your guess so far. You have {len(heartlist)} "\u2764"  left.'
            elif len(heartlist) > 0:
                heartlist.pop()
                message = f"Wrong. Only {len(heartlist)} \"\u2764\" left \n {' '.join(clue_list)}"
                if len(heartlist)==0:
                     message = f"You lost! The word was: {the_word}"
            else:
                message = f"You lost! The word was: {the_word}"

            if '?' not in clue_list:
                message = 'Well done! The word was: ' + ' '.join(clue_list)

        session['clue_list'] = clue_list
        session['heartlist'] = heartlist
    else:
        message = ''

    return render_template("home.html", message=message,the_word=len(session['the_word']))

@app.route('/new_word', methods=['POST'])
def new_word():
    initialize_game()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

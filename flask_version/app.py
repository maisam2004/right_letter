from flask import Flask,redirect,render_template,request,url_for,session
from class_play import let_guess
app = Flask(__name__)

@app.route('/',methods = ['get','post'])
def home():
    if request.method != 'post':
        return render_template('home.html')
    letter = request.form['letter']
    start = let_guess(letter)

    


    

if __name__ == "__main__":
    app.run(debug=True)
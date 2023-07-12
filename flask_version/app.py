from flask import Flask,redirect,render_template,request,url_for,aport,session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
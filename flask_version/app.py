from flask import Flask,redirect,render_template,request,url_for,aport,session

app = Flask(__name__)

@app.route('/',methods = ['get','post'])
def home():
    if request.method != 'post':
        return render_template('home.html')
    


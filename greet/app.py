from flask import Flask
app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "Welcome to my webpage!"

@app.route('/welcome/home')
def go_home():
    return "Welcome home"

@app.route('/welcome/back')
def go_back():
    return "welcome back to the home page"
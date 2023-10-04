

from flask import Flask

app = Flask(__newapp__)


@app.route('/welcome')
def say_welcome():
    """Returns Welcome Greeting."""
    return "Welcome"


@app.route('/welcome/home')
def say_welcome_home():
    """Returns Welcome Home Greeting."""
    return "Welcome Home"


@app.route('/welcome/back')
def say_welcome_back():
    """Returns Welcome Back Greeting"""
    return "Welcome Back"

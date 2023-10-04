
from flask import Flask, request

app = Flask(__calcapp__)


@app.route('/add')
def add(a, b):
    """Returns a + b"""
    return a + b


@app.route('/sub')
def subtract(a, b):
    """Returns a - b"""
    return a - b


@app.route('/mult')
def multiply(a, b):
    """Returns a * b"""
    return a * b


@app.route('/div')
def divide(a, b):
    """Returns a / b"""
    return a / b

#!/usr/bin/python3
"""Minimal flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_flask():
    """Route index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Route c"""
    return "c %s" % text.replace("_", " ")


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)

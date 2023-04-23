#!/usr/bin/python3

"""
Flask App

Routes:
    /
    /hbnb
    /c/<text>
    /python/(<text>)
    /number/<int:n>
"""

from flask import Flask, abort
app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Number Route 🔢"""
    return "%i is a number" % n


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Python Route 🐍"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """C Route :)"""
    return 'C ' + text.replace('_', ' ')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page"""
    return "HBNB"


@app.route('/', strict_slashes=False)
def hello_world():
    """Website index page"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

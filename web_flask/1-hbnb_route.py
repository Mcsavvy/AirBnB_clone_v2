#!/usr/bin/python3

"""
Flask App

Routes:
    /
    /hbnb
"""

from flask import Flask
app = Flask(__name__)


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

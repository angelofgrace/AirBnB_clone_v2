#!/usr/bin/python3
""" Start a Flask web app """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def title():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_string(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<string:text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_string(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>', strict_slashes=False)
def numeral(n):
    if n.isnumberic():
        return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run()

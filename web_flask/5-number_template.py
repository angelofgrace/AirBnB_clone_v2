#!/usr/bin/python3
""" Start a Flask web app """


from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def numeral(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbered_template(n):
    return render_template('5-number', number=n)


if __name__ == "__main__":
    app.run()

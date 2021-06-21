#!/usr/bin/python3
""" Start a Flask web app """

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
	return 'Hello HBNB!'

if __name__ == "__main__":
	app.run()

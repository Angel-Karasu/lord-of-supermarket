#!/bin/python
from flask import Flask, render_template

HOST = '0.0.0.0'
PORT = 5500

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/search/')
def search_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
#!/bin/python
from flask import Flask, render_template, request

from supermarkets_scraper.supermarkets.intermarche import INTERMARCHES

intermarche = INTERMARCHES.get_supermarkets_by_postal_code(38100)[0]

HOST = '0.0.0.0'
PORT = 5500

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@app.route('/search/', methods=['POST'])
def search():
    req = request.get_json()
    return [vars(product) for product in intermarche.search_products(req['search'], req['page'], req['sort'], req['order'])]

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
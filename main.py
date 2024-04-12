#!/bin/python
from flask import Flask, render_template, request

from supermarkets_scraper.supermarkets.intermarche import INTERMARCHES

HOST = '0.0.0.0'
PORT = 5500

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@app.route('/search/', methods=['POST'])
def search():
    req = request.get_json()
    return {
        i: [vars(product) for product in products]
        for i, products in INTERMARCHES.search_products(req['list_index_supermarket'], req['search'], req['page'], req['sort'], req['order']).items()
    }

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
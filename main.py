#!/bin/python
from flask import Flask, render_template, jsonify

# from supermarkets_scraper.supermarkets.intermarche import INTERMARCHES
from supermarkets_scraper.utils.product import Product 

HOST = '0.0.0.0'
PORT = 5500

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@app.route('/search/<string:product>/<int:page>/<string:sort>/<string:order>/')
def search(product:str, page:int, sort:str, order:str):
    print(product, page, sort, order)
    return jsonify(vars(Product('', '', '', 0, 0, '', '')))

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
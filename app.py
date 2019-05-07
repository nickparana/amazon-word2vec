from flask import Flask, render_template, jsonify, request
import os
import json
import AmazonLoadModel

app = Flask(__name__)


@app.route("/products/", methods=['GET'])
def get_products():
    if request.method == 'GET':
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/data", "products_list.json")
        data = json.load(open(json_url))
        return jsonify(data)


@app.route("/products/<product_asin>", methods=['GET'])
def get_product_by_asin(product_asin):
    if request.method == 'GET':
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/data", "products_list.json")
        data = json.load(open(json_url))
        return jsonify(data)


@app.route("/products/<product_asin>/best", methods=['GET'])
def get_n_recommendations_for_product(product_asin):
    if request.method == 'GET':
        asin = product_asin
        top_n = request.args.get('topN', default=5, type=int)
        return jsonify(AmazonLoadModel.get_top_n(asin, top_n))


@app.route("/products/categories", methods=['GET'])
def get_categories():
    if request.method == 'GET':
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/data", "categories.json")
        data = json.load(open(json_url))
        return jsonify(data)


app.run()

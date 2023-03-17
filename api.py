

from flask import Flask, jsonify, request, Response
import json
from flask_cors import CORS

from dataN1 import response as resn1
from dataN1 import stationsAndPricesN1

from dataAtlantsolia import response as resatlanso
from dataAtlantsolia import stationsAndPricesAO

from dataOB import response as respob
from dataOB import stationsAndPricesOB

from scrapOrkan import results as respork
from scrapOlis import totalStationsInDict as respolis

app = Flask(__name__)
CORS(app)


@app.route('/n1', methods=['GET'])
def n1():
    data = stationsAndPricesN1(resn1)
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data, content_type='application/json; charset=utf-8')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/atlanso', methods=['GET'])
def atlansolia():
    data = stationsAndPricesAO(resatlanso)
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data, content_type='application/json; charset=utf-8')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/ob', methods=['GET'])
def ob():
    data = stationsAndPricesOB(respob)
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data, content_type='application/json; charset=utf-8')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/orkan', methods=['GET'])
def orkan():
    data = respork
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data, content_type='application/json; charset=utf-8')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/olis', methods=['GET'])
def olis():
    data = respolis
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data, content_type='application/json; charset=utf-8')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


if __name__ == '__main__':
    app.run(debug=True)

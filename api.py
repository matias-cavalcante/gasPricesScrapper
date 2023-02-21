

from flask import Flask, jsonify, request
from flask_cors import CORS
import PypeteerAPP

app = Flask(__name__)
CORS(app)


@app.route('/n1', methods=['GET'])
def hello():
    responseGas = PypeteerAPP.response
    jsonito = PypeteerAPP.n1Data(responseGas)
    return jsonito


if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, jsonify, request
from flask_cors import CORS
import scrapN1

app = Flask(__name__)
CORS(app)


@app.route('/n1', methods=['GET'])
def hello():
    n1Data = scrapN1.clickAndFetch()
    n1JsonNow = jsonify(n1Data)
    return n1JsonNow


if __name__ == '__main__':
    app.run(debug=True)

# flask --app serve run
# https://flask.palletsprojects.com/en/3.0.x/quickstart/

from flask import Flask, jsonify, request
import app_algoritmo

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    paylo = request.get_json()
    print(paylo)
    return "Hello, World!"

# Method with query parameters to get the data (recive the number of songs to recommend)
@app.route("/recommend", methods=['GET'])
def recommend():
    # Getting the number of songs to recommend
    n = request.args.get("n", 10)
    return jsonify(app_algoritmo.recommend(int(n)))
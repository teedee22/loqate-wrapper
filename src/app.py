from loqate import Geocoding_International_Geocode_v1_10 as latlong

from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/")
def hello_gitlab():
    message = "Hello, Healthcheck confirms proxy up and running"
    payload = {"message": message}
    return jsonify(payload)

@app.route("/loqate", methods=['POST'])
def new():
    data = request.json
    countrycode = data['countrycode']
    postcode = data['postcode']
    secretkey = data['secretkey']
    return jsonify(latlong(secretkey, countrycode, postcode))

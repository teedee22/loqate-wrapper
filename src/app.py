from loqate import Geocoding_International_Geocode_v1_10 as latlong

from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/")
def healthcheck():
    message = "Healthcheck working"
    payload = {"message": message}
    return jsonify(payload)

@app.route("/loqate", methods=['POST'])
def new():
    data = request.json
    countrycode = data['countrycode']
    postcode = data['postcode']
    secretkey = data['secretkey']
    return jsonify(latlong(secretkey, countrycode, postcode))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)
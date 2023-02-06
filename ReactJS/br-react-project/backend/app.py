from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def get_articles():
    # file = open("json_hourly_demo.json","r")
    # file = open("json_hourly_demo.json","r")
    # data = json.load(file)

    # return data

    return jsonify({
    "date":"01/01/2021",
    "time":"22:00",
    "gl":"1",
    "uscm":"23"
})



if __name__ == "__main__":
    app.run(debug=True)
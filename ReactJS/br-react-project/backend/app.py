from flask import Flask, jsonify
from flask_cors import CORS
<<<<<<< Updated upstream
import datetime
import time
import pytz
=======
>>>>>>> Stashed changes

app = Flask(__name__)
CORS(app)

<<<<<<< Updated upstream
time_now = datetime.datetime.now()

@app.route("/", methods = ["GET"])
def get_articles():
    global time_now
    return jsonify({
    "date":time_now.strftime('%a %d-%m-%Y %H:%M:%S'),
    "time":"22:00",
    "gl":1,
    "uscm":25
=======
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
>>>>>>> Stashed changes
})



if __name__ == "__main__":
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes
    app.run(debug=True)
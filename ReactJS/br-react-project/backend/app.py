from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import time
import schedule

app = Flask(__name__)
CORS(app)

# time_now = datetime.datetime.now()

@app.route("/", methods = ["GET"])
def get_articles():
    time_now = datetime.datetime.now()
    return jsonify({
    "date":time_now.strftime('%a %d-%m-%Y'),
    "time":time_now.strftime('%H:%M:%S'),
    "gl":1,
    "uscm":25
})



if __name__ == "__main__":
    # Always runs in while(1)
    app.run(debug=True)
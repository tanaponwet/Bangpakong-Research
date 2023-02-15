from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import random
import json
from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO, emit

import eventlet
eventlet.monkey_patch(thread=True, time=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bangpakong'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app=app, cors_allowed_origins='*',
                    logger=True, engineio_logger=True)
scheduler = BackgroundScheduler(executor='gevent')


# @app.route('/', methods=["GET"])
# def send_first():
#     with app.app_context():
#         time_now = datetime.datetime.now()
#         data = {   
#             "current": {
#                     "date": "999",
#                     "time": "99:99",
#                     "gl": 112,
#                     "uscm": 11200
#         }}
#         return jsonify(data)


@app.route('/', methods=["GET"])
@ socketio.on("post_hourly", namespace="/hourly")
def post_hourly():
    with app.app_context():
        time_now = datetime.datetime.now()
        data = {
            "current": {
                "date": time_now.strftime('%a %d-%m-%Y'),
                "time": time_now.strftime('%H:%M:%S'),
                "gl": round(random.uniform(1, 20), 2),
                "uscm": round(random.uniform(1, 20000), 2)
            }

        }
        data_json = json.dumps(data)
        print("Hourly sent:", time_now)
        socketio.emit("post_hourly", data_json,
                      broadcast=True, namespace="/hourly")
        return jsonify(data)


if __name__ == '__main__':
    with app.app_context():
        scheduler.add_job(post_hourly, "cron", second="*/10")
        # scheduler.add_job(post_hourly, "cron", hour="*", minute="0", second="0")
        scheduler.start()
        socketio.run(app, debug=True)

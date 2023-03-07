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

def read_from_meter(time_now):
    date_file = time_now.strftime("%Y%m%d")
    time_file = int(time_now.strftime("%H%M"))
    text = open(r'C:\Users\Administrator\Documents\GET\from-meter\meter-{}-{:04d}10.json'.format(date_file, time_file))
    data_from_meter = json.load(text)

    uscm = data_from_meter["Sensor"]["EC"] * 1000

    data = {
            "date": time_now.strftime('%a %d-%m-%Y'),
            "time": time_now.strftime('%H:%M:00'),
            "uscm": uscm,
            "gl": round(uscm * .55 / 1000,2)
        }
    return data


@app.route('/', methods=["GET"])
@socketio.on("post_hourly", namespace="/hourly")
def post_hourly():
    with app.app_context():
        time_now = datetime.datetime.now()
        data = {
            "current": {},
            "next_24":[],
            "comp_chol_meter":[]
        }

        data["current"] = read_from_meter(time_now)

        for i in range(1, 24+1):
            time_in_24h = (time_now + datetime.timedelta(hours=i)).strftime('%H:%M:%S')
            data_for_next_24h = {
            "date": time_now.strftime('%a %d-%m-%Y'),
            "time": time_in_24h,
            "gl": round(random.uniform(1, 20), 2),
            "uscm": round(random.uniform(1, 20000), 2)
            }
            data["next_24"].append(data_for_next_24h)

        data_json = json.dumps(data)

        print("Hourly sent:", time_now)
        socketio.emit("post_hourly", data_json,
                      broadcast=True, namespace="/hourly")
        return jsonify(data)


if __name__ == '__main__':
    with app.app_context():
        # scheduler.add_job(post_hourly, "cron", second="*/10")
        scheduler.add_job(post_hourly, "cron", minute="*", second="15")
        # scheduler.add_job(post_hourly, "cron", hour="*", minute="6", second="10")
        scheduler.start()
        socketio.run(app, debug=True, port=20001, host="0.0.0.0")

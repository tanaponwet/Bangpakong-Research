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


report = {
    "current": {},
    "next_24":[],
    "comp_chol_meter":[]
}


def read_from_meter(time):
    date_file = time.strftime("%Y%m%d")
    time_file = int(time.strftime("%H"))
    text = open(r'C:\Users\Administrator\Documents\GET\from-meter\meter-{}-{:02d}0010.json'.format(date_file, time_file))
    data_from_meter = json.load(text)

    uscm = data_from_meter["Sensor"]["EC"] * 1000
    gl = round(uscm * .55 / 1000,2)

    data = {
            "date": time.strftime('%a %d-%m-%Y'),
            "time": time.strftime('%H:00'),
            "uscm": uscm,
            "gl": gl
        }

    return data, gl


def read_from_bangkla(time):
    date_file = time.strftime("%Y%m%d")
    time_file = int(time.strftime("%H"))
    text = open(r'C:\Users\Administrator\Documents\GET\cholpratan-bangkla\SP07-{}-{:02d}00.json'.format(date_file, time_file))
    data_from_bangkla = json.load(text)
    try:
        gl_bangkla = float(data_from_bangkla[0]["Salinity"])
    except:
        gl_bangkla = None
    
    return gl_bangkla


def merge_bangkla_meter(time):

    data = {
        "date": time.strftime("%d-%m"),
        "time": time.strftime("%H:00"),
        "meter": read_from_meter(time)[1],
        "bangkla": read_from_bangkla(time)
    }
    return data


def gen_next_demo(time):
    data = {
            "date": time.strftime('%a %d-%m-%Y'),
            "time": time.strftime('%H:00'),
            "gl": round(random.uniform(0, 3), 2),
            "uscm": round(random.uniform(1, 20000), 2)
            }
    return data

# def merge_demo(time):
#     data = {
#         "date": time.strftime("%d-%m"),
#         "time": time.strftime("%H:%M"),
#         "meter": round(random.uniform(2000, 20000), 2),
#         "bangkla": round(random.uniform(2000, 20000), 2)
#     }
#     return data


time_now = datetime.datetime.now()

report["current"] = read_from_meter(time_now)[0]


for i in range(1, 24 +1):
    time_next = (time_now + datetime.timedelta(hours=i))
    time_prev = (time_now - datetime.timedelta(hours=(i - 1)))


    report["comp_chol_meter"].insert(0,merge_bangkla_meter(time_prev))
    report["next_24"].append(gen_next_demo(time_next))


@app.route('/', methods=["GET"])
def first_entrance():
    with app.app_context():  
        return jsonify(report)


@socketio.on("post_hourly", namespace="/hourly")
def post_hourly():
    with app.app_context():
        time_now = datetime.datetime.now()


        report["current"] = read_from_meter(time_now)[0]

        report["next_24"] = [][:]

        # if len(report["comp_chol_meter"]) > 0:
        report["comp_chol_meter"].pop(0)
        
        report["comp_chol_meter"].append(merge_bangkla_meter(time_now))


        for i in range(1, 24+1):
            time_next = (time_now + datetime.timedelta(hours=i))
            report["next_24"].append(gen_next_demo(time_next))

        data_json = json.dumps(report)

        print("Hourly sent:", time_now)
        socketio.emit("post_hourly", data_json,
                      broadcast=True, namespace="/hourly")
        # return jsonify(report)


if __name__ == '__main__':
    with app.app_context():
        # scheduler.add_job(post_hourly, "cron", second="*/10")
        # scheduler.add_job(post_hourly, "cron", minute="*", second="15")
        scheduler.add_job(post_hourly, "cron", hour="*", minute="6", second="15")
        scheduler.start()
        socketio.run(app, debug=True, port=20001, host="0.0.0.0")

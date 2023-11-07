from flask import Flask, render_template
import datetime
import psutil


app = Flask(__name__)


def get_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d @ %X")


def get_battery():
    battery_sensors = psutil.sensors_battery()
    if battery_sensors is None:
        return 100
    else:
        return battery_sensors.percent


@app.route("/")
def index():
    time_now = get_datetime()
    battery = get_battery()
    return render_template("index.html", time_now=time_now, battery=battery)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

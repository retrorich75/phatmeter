#!/usr/bin/python

from flask import Flask, jsonify, redirect, render_template
from envirophat import analog, motion, leds, light, weather


def get_sensor_data():
	data = {}
	data['analog'] = analog.read_all()
	data['accelerometer'] = tuple(motion.accelerometer())
	data['heading'] = motion.heading()
	data['leds'] = leds.is_on()
	data['light'] = light.light()
	data['rgb'] = light.rgb()
	data['pressure'] = weather.pressure()
	data['temperature'] = weather.temperature()
	return data


app = Flask(__name__)

@app.route('/')
def index():
	data = get_sensor_data()
	return render_template('index.html', data=sorted(data.items()))

@app.route('/download')
def download():
	return jsonify(get_sensor_data())

@app.route('/leds_off')
def leds_off():
	leds.off()
	return redirect('/')

@app.route('/leds_on')
def leds_on():
	leds.on()
	return redirect('/')


if __name__ == '__main__':
	leds.off()
	app.run(debug=False, host='0.0.0.0')

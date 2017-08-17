#!/usr/bin/python

from envirophat import analog, motion, light, weather
from paho.mqtt import publish
import time

def publish_sensor_data(hostname, root):
	messages = []
	for i, data in enumerate(analog.read_all()):
		messages.append(('%s/analog/%d' % (root, i), str(data), 0, True))
	messages.append((root+'/light/light', str(light.light()), 0, True))
	messages.append((root+'/light/rgb', str(light.rgb()), 0, True))
	messages.append((root+'/motion/accelerometer', str(motion.accelerometer()), 0, True))
	messages.append((root+'/motion/heading', str(motion.heading()), 0, True))
	messages.append((root+'/weather/pressure', str(weather.pressure()), 0, True))
	messages.append((root+'/weather/temperature', str(weather.temperature()), 0, True))
	publish.multiple(messages), hostname=hostname)

if __name__ == '__main__':
	hostname = 'iot.eclipse.org'
	root = 'envirophat'
	while True:
		publish_sensor_data(hostname, root)
		time.sleep(10)

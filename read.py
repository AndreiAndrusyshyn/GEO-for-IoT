
import csv
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(18, gpio.OUT)

gpio.output(18, gpio.LOW)
time.sleep(1)
with open('DB.csv', 'r') as csvFile:

	while True:
		where = csvFile.tell()
		line = csvFile.readline()
		if not line:
			time.sleep(4)
			csvFile.seek(where)
		else:
			if int(line) < 300:
				gpio.output(18, gpio.HIGH)
				print("yes")
				print(line)
			else:
				print(line)
				gpio.output(18, gpio.LOW)


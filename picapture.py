#! /usr/bin/env python3
#2photosample.py

import picamera

import time
#import date
import RPi.GPIO as GPIO

#GPIO.cleanup()
PICTURE_WIDTH = 800
PICTURE_HEIGHT = 600

INTAVAL = 600
value = 817

SLEEPTIME = 10
#sleeptime : time between photos
CHECKTIME = 10
#checktime : still sensor ON?

SENSOR_PIN = 9
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
cam = picamera.PiCamera()

cam.resolution = (PICTURE_WIDTH,PICTURE_HEIGHT)
cam.resolution = (640, 480)

st = time.time() - INTAVAL
i = 0

while True:
	if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
		time.sleep(CHECKTIME)
		if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
			i =i+1
			st =time.time()
			filename = time.strftime("%Y%m%d%H%M%S") + '.jpg'
			cam.capture('/home/pi/Desktop/%s.jpg' %filename)	
			time.sleep(SLEEPTIME)
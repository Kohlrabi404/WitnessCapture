#! /usr/bin/env python3

import picamera
from pathlib import Path
import time
import subprocess
#import date
import RPi.GPIO as GPIO

class Data :
	def __init__(self):
		#GPIO.cleanup()
		self.PICTURE_WIDTH = 800
		self.PICTURE_HEIGHT = 600
		self.INTAVAL = 600

		self.SLEEPTIME = 10
		#sleeptime : time between photos
		self.CHECKTIME = 10
		#checktime : still sensor ON?
		self.WAITTIME = 10

		SENSOR_PIN = 9
		GPIO.cleanup()

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(SENSOR_PIN, GPIO.IN)
		self.cam = picamera.PiCamera()

		self.cam.resolution = (self.PICTURE_WIDTH,self.PICTURE_HEIGHT)
		self.cam.resolution = (640, 480)
	
	def get_pic_and_vid(self):
		while True : 
			if GPIO.input(self.SENSOR_PIN) == GPIO.HIGH:
				time.sleep(self.CHECKTIME)
				if GPIO.input(self.SENSOR_PIN) == GPIO.HIGH:
					# Create Image file
					directory = Path.cwd()/"data"
					fname = time.strftime("%Y-%m-%d %H:%M:%S")
					picname = fname + '.jpg'
					self.cam.capture(directory/picname)
					time.sleep(self.SLEEPTIME)


					# Create Video file
					vidname = 'video' + time.strftime("%Y-%m-%d %H:%M:%S")
					vidname_mp4 = vidname + ".mp4"
					vidname_h264 = vidname + ".h264"
					self.cam.start_recording(directory/vidname_h264)
					time.sleep(self.WAITTIME)
					self.cam.stop_recording()
					time.sleep(self.SLEEPTIME)
					# Convert to mp4
					cmd = f"MP4Box -add {directory/vidname_h264} {directory/vidname_mp4}"
					subprocess.call(cmd, shell=True)

					return [fname, str(directory/picname), str(directory/vidname_mp4)]
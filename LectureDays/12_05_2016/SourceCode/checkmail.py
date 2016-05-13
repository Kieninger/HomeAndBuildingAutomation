#!/usr/bin/env python

USERNAME = "kieninger.florian@gmail.com"
PASSWORD = "lbbjCQj6"

import RPi.GPIO as GPIO
import feedparser
import time

GPIO.setwarnings(False)

while True:
	GPIO_PIN_YELLOW = 18
	GPIO_PIN_RED = 23
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_PIN_YELLOW, GPIO.OUT)
	GPIO.setup(GPIO_PIN_RED, GPIO.OUT)
	newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")['feed']['fullcount'])
	if newmails > 0:
		GPIO.output(GPIO_PIN_YELLOW, False)
		#GPIO.output(GPIO_PIN_RED, False)
	else:
		GPIO.output(GPIO_PIN_YELLOW, True)
		#GPIO.output(GPIO_PIN_RED, True)
	print "sleeping"
	time.sleep(1)

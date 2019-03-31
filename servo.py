import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

try:
	while True:
    		p.ChangeDutyCycle(2.5)
    		raw_input("press enter to exit")
		p.stop()
		raw_input("press")
		p.start(12.5)
    		p.ChangeDutyCycle(12.5)
		raw_input("press")
		p.stop()
    		raw_input("press enter to exit")
    		p.ChangeDutyCycle(12.5)
    		raw_input("press enter to exit")
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

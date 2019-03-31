  
from gpiozero import Button
from picamera import PiCamera
from time import sleep
from signal import pause
from main2 import detect_labels as dL
from stepper import clockWise90 as cw90
from stepper  import coClock90 as c90
import RPi.GPIO as GPIO
import time

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)

camera = PiCamera()

path = "/home/pi/Desktop/hackPhotos/hackImage.jpg"
#start the camera
#camera.rotation = 180
#camera.start_preview()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
#def stop_camera():
 #   camera.stop_preview()
    #exit the program
  #  exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    sleep(3)
    camera.capture('/home/pi/Desktop/hackPhotos/hackImage.jpg')
    print('A photo has been taken')
    #sleep(3)
    tCan = dL(path)
    if (tCan == "compost"):
	GPIO.cleanup()
	c90()
	sleep(5)
	GPIO.cleanup()
	cw90()
    else:
	GPIO.cleanup()
	cw90()
	sleep(5)
	GPIO.cleanup()
	c90()
    sleep(5)

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Calibrating....."
time.sleep(2)

print "Place the object......"

try:
    #print "inside try"
    while True:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)

       #print "before while loop"
       while GPIO.input(ECHO)==0:
          pulse_start = time.time()
       #print "post 1st while"
       while GPIO.input(ECHO)==1:
          pulse_end = time.time()

       #print "post 2nd while"
       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150

       distance = round(distance+1.15, 2)

       print distance
       if distance<=18 and distance>=5:
          print "distance:",distance,"cm"
          i=1
          take_photo()
	  time.sleep(1)
	  GPIO.setup(TRIG, GPIO.OUT)
	  GPIO.setup(ECHO, GPIO.IN)
	  continue
       if distance>18 and i==1:
          print "place the object...."
          i=0
       time.sleep(2)

except KeyboardInterrupt:
     GPIO.cleanup()

#assign a function that runs when the button is pressed
#button.when_pressed = stop_camera

#pause()



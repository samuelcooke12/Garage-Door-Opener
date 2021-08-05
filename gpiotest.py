import RPi.GPIO as GPIO
import time
outPin = 5


GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)


try:
    while True:
       GPIO.output(outPin, GPIO.HIGH)
       print("On")
       time.sleep(3)
       GPIO.output(outPin, GPIO.LOW)
       print("Off")
       time.sleep(3)
      
except KeyboardInterrupt:
    
    GPIO.cleanup()
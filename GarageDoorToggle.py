import time
import RPi.GPIO as GPIO

user = ""
outPin=5
inPin = 12

while(user != "0"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outPin,GPIO.OUT)
    GPIO.setup(inPin, GPIO.IN)
    
    
    if GPIO.input(inPin) == True:
            
            status="open"
            
    else:
            
            status="closed"
    user = input("Press 1 to toggle garage door... Garage is " + status + "... Press 2 to check status again... Press 0 to exit\n")
    if(user == "1"):
        
        print("Toggling garage...")
        
        GPIO.output(outPin, GPIO.HIGH)
        time.sleep(.3)
        GPIO.output(outPin, GPIO.LOW)
        GPIO.cleanup()
    if(user == "2"):
        if GPIO.input(inPin) == True:
            
            status="open."
            
        else:
            
            status="closed."
        print("The Garage is " + status)
print("Cleaning up...")       
GPIO.cleanup()

    
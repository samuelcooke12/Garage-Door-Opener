from flask import Flask, render_template, request, Response
import cv2
import time
import RPi.GPIO as GPIO

app = Flask(__name__, static_url_path='/static')

camera = cv2.VideoCapture(0)

def gen_frames():
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    
    return render_template('index.html', garageStatus=getGarageStatus(), buttonValue=getButtonStatus())

def getGarageStatus():
    inPin = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inPin, GPIO.IN)
    if GPIO.input(inPin) == True:
            print("Short Detected")
            status="closed"
            
    else:
            print("No Short Detected")
            status="open"
    GPIO.cleanup()
    return status 
def getButtonStatus():
    inPin = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inPin, GPIO.IN)
    if GPIO.input(inPin) == True:
            print("Short Detected")
            status="Open"
            
    else:
            print("No Short Detected")
            status="Close"
    GPIO.cleanup()
    return status       


@app.route('/', methods=['POST'])
def my_form_post():
    outPin=5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outPin,GPIO.OUT)
    GPIO.output(outPin, GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(outPin, GPIO.LOW)
    GPIO.cleanup()
    return render_template('index.html', garageStatus=getGarageStatus(), buttonValue=getButtonStatus())



 
   



if __name__ == '__main__':
    app.run(host='0.0.0.0')
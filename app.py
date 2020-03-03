#!/usr/bin/env python
from flask import Flask, render_template, Response, request
from subprocess import call
# emulated camera
# from ObjectDetection import DetectObjectsWebcam
from camera import VideoCamera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')



def gen(vd):
    """Video streaming generator function."""
    while True:
        # frame = DetectObjectsWebcam()
        frame = vd.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    x =  Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    # print(x)
    return x


@app.route('/message', methods=['POST'])
def message():
    msg = request.form['chat']
    print(msg)
    call(["espeak","-s140 -ven+18 -z",msg])
    return ' ',205
if __name__ == '__main__':
    app.run(debug=True, threaded=True)

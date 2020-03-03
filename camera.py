from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    _time=0
    def __init__(self):
        self._time=int(time())
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        print(self._time-int(time()))
        return self.frames[int(time()) % 3]
import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('fortnite.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        # cv2.imshow('image')
        image = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    

#import numpy as np

# Playing video from file:
# cap = cv2.VideoCapture('vtest.avi')
# Capturing video from webcam:


if __name__ == '__main__':
    C = Camera()
    for i in range(100):
        C.get_frame()

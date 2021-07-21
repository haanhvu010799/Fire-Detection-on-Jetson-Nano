import os
import time
import argparse
import numpy as np
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver
from flask import Flask, render_template, Response, flash

import app as ap
app = Flask(__name__)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
    
def gen():
    
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('detect.jpeg', 'rb').read() + b'\r\n')
        time.sleep(0.05)           
            
     
@app.route('/video_feed')
def video_feed():
	return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
                    
if __name__ == '__main__':
    app.run(host='192.168.1.9',port=5000,debug=True)
               
               

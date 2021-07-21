"""trt_yolo.py

This script demonstrates how to do real-time object detection with
TensorRT optimized YOLO engine.
"""

import paho.mqtt.client as mqtt 
import json
import psutil
import os
import time
import argparse
import numpy as np
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA drive
from flask import Flask, render_template, Response, flash

from utils.yolo_classes import get_cls_dict
from utils.camera import add_camera_args, Camera
from utils.display import open_window, set_display, show_fps
from utils.visualization import BBoxVisualization
from utils.yolo_with_plugins import TrtYOLO

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ACCESS_TOKEN='Z9Stg528gboR63ONctBB'                 
THINGSBOARD_HOST='192.168.1.6'
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
fire_data={'firerate': 0,'ViTri': 0 ,'Thong Bao' : 'Chua gui email canh bao', 'FPS': 0, 'count': 3,}


# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

#MQTT cho mail server



def parse_args():
    """Parse input arguments."""
    desc = ('Capture and display live camera video, while doing '
            'real-time object detection with TensorRT optimized '
            'YOLO model on Jetson')
    parser = argparse.ArgumentParser(description=desc)
    parser = add_camera_args(parser)
    parser.add_argument(
        '-c', '--category_num', type=int, default=1,
        help='number of object categories [80]')
    parser.add_argument(
        '-m', '--model', type=str,default='yolov4-tiny-416' ,required=True,
        help=('[yolov3-tiny|yolov3|yolov3-spp|yolov4-tiny|yolov4|'
              'yolov4-csp|yolov4x-mish]-[{dimension}], where '
              '{dimension} could be either a single number (e.g. '
              '288, 416, 608) or 2 numbers, WxH (e.g. 416x256)'))
    parser.add_argument(
        '-l', '--letter_box', action='store_true',
        help='inference with letterboxed image [False]')
    args = parser.parse_args()
    return args


def loop_and_detect(cam, trt_yolo, conf_th, vis):
    client.loop_start()
    fps = 0.0
    count = 3
    tic = time.time()
    while True:
        
        #Tinh trang phan cung
        #print('CPU da dung ', psutil.cpu_percent(4))
        #fire_data['CPU']= psutil.cpu_percent(4)
        #print('RAM memory % used:', psutil.virtual_memory()[2])
        #fire_data['RAM']=psutil.virtual_memory()[2]
        img = cam.read()
        frame= cam.read()
       	
        boxes, confs, clss = trt_yolo.detect(img, conf_th)
        vitri= confs.size
        arraycheck=np.sum(confs) 
        img = vis.draw_bboxes(img, boxes, confs, clss)
        result = np.asarray(img)
        #ghi file
        img = show_fps(img, fps)
        cv2.imwrite('detect.jpeg',frame)
        if(arraycheck>0) :
            fire_data['Thong Bao'] = 'Camera da phat hien ra lua'
            firerate=round(np.max(confs)*100,2)
            count= count - 1
            if (count < 0):
            	count=0
            if( firerate > 70 and count < 3):
                fire_data['Thong Bao'] = 'Email canh bao da duoc gui di'
                fire_data['count']= count
            print("Kha nang da xay ra hoa hoan: ",firerate,"%")
            print("So vi tri dang xay ra hoa hoan: ",vitri) 
            fire_data['firerate'] = firerate
            fire_data['ViTri']= vitri
            fire_data['FPS']= fps;
            client.publish('v1/devices/me/telemetry', json.dumps(fire_data), 1)
        #cv2.imshow(WINDOW_NAME, img)
        toc = time.time()
        curr_fps = 1.0 / (toc - tic)
        # Tinh fps trung binh
        fps = curr_fps if fps == 0.0 else (fps*0.95 + curr_fps*0.05)
        tic = toc
        
def main():
    args = parse_args()
    cam = Camera(args)
    fire_data['Thong Bao'] = 'Camera bat dau hoat dong'
    cls_dict = get_cls_dict(args.category_num)
    vis = BBoxVisualization(cls_dict)
    trt_yolo = TrtYOLO(args.model, args.category_num, args.letter_box)

    #open_window(WINDOW_NAME, 'Fire Detection',cam.img_width, cam.img_height)
    loop_and_detect(cam, trt_yolo, conf_th=0.3, vis=vis)
    cam.release()
    #cv2.destroyAllWindows()


        

if __name__ == '__main__':
    main()

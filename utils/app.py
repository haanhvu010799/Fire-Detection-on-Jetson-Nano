"""trt_yolo.py

This script demonstrates how to do real-time object detection with
TensorRT optimized YOLO engine.
"""


import os
import time
import argparse
import numpy as np
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver
from flask import Flask, render_template, Response, flash

from utils.yolo_classes import get_cls_dict
from utils.camera import add_camera_args, Camera
from utils.display import open_window, set_display, show_fps
from utils.visualization import BBoxVisualization
from utils.yolo_with_plugins import TrtYOLO


WINDOW_NAME = 'Fire Detection'
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
    """Continuously capture images from camera and do object detection.

    # Arguments
      cam: the camera instance (video source).
      trt_yolo: the TRT YOLO object detector instance.
      conf_th: confidence/score threshold for object detection.
      vis: for visualization.
    """
    #full_scrn = False
    fps = 0.0
    count = 0
    guiemail = 0
    tic = time.time()
    while True:
        
        img = cam.read()
        frame= cam.read()
       
        boxes, confs, clss = trt_yolo.detect(img, conf_th)
        arraycheck=np.sum(confs) 
        img = vis.draw_bboxes(img, boxes, confs, clss)
        result = np.asarray(img)
        img = show_fps(img, fps)
        if(arraycheck>0) :
            firerate=round(np.max(confs)*100,2)
            count = count + 1
            if ( count > 50):
            	guiemail = 1
            	print("Da gui email")
            	count = 0
            guiemail = 0
            print("Kha nang da xay ra hoa hoan: ",firerate,"%")
        #cv2.imshow(WINDOW_NAME, img)
        #ghi file
        cv2.imwrite('detect.jpg',frame)
        toc = time.time()
        curr_fps = 1.0 / (toc - tic)
        # Tinh fps trung binh
        fps = curr_fps if fps == 0.0 else (fps*0.95 + curr_fps*0.05)
        tic = toc
        key = cv2.waitKey(1)
        
        
    
def main():
    args = parse_args()
    if args.category_num <= 0:
        raise SystemExit('ERROR: bad category_num (%d)!' % args.category_num)
    if not os.path.isfile('yolo/%s.trt' % args.model):
        raise SystemExit('ERROR: file (yolo/%s.trt) not found!' % args.model)

    cam = Camera(args)
    if not cam.isOpened():
        raise SystemExit('ERROR: failed to open camera!')

    cls_dict = get_cls_dict(args.category_num)
    vis = BBoxVisualization(cls_dict)
    trt_yolo = TrtYOLO(args.model, args.category_num, args.letter_box)

    #open_window(WINDOW_NAME, 'Fire Detection',cam.img_width, cam.img_height)
    loop_and_detect(cam, trt_yolo, conf_th=0.3, vis=vis)

    cam.release()
    #cv2.destroyAllWindows()


        

if __name__ == '__main__':
    main()

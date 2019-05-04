# -----------------
# MODULES
# -----------------

# main modules
import yaml
import numpy as np
import cv2
import os
from time import sleep
from threading import Timer
import argparse
drom colors import *

# custom modules
from modules.config import config,fn,fn_yaml,fn_out
from modules.init_parking import init_parking
from modules.init_parking_data import cap,video_info
from modules.parking_detection import parking_detection
from modules.keyboard_options import keyboard_options
#from modules.export_reading_in_file import export_reading_in_file
from modules.coordinates_generator import CoordinatesGenerator

# ------------------------------------------------------------------------------------

# -----------------
# CORE
# -----------------

parking_bounding_rects = []

# Read YAML data (parking space polygons)
with open(fn_yaml, 'r') as stream:
    parking_data = yaml.load(stream)

# Init parking data
init_parking(parking_data, parking_bounding_rects)

pk_status = [False] * len(parking_data)
parking_buffer = [None] * len(parking_data)

# during app is running
while(cap.isOpened()):
    spot = 0
    occupied = 0
    array_of_free_spaces = []
    
    # Read frame-by-frame
    video_cur_pos = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0 # Current position of the video file in seconds
    video_cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) # Index of the frame to be decoded/captured next
    ret, frame = cap.read()

    if ret == False:
        print("Capture Error")
        break
    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_RED)
            generator.generate()

    with open(data_file, "r") as data:
        points = yaml.load(data)
        detector = MotionDetector(args.video_file, points, int(start_frame))
        detector.detect_motion()

    # Background Subtraction
    f_bluring = cv2.GaussianBlur(frame.copy(), (5,5), 3)
    f_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)
    f_out = frame.copy()

    # detect parking (Background Subtraction)
    parking_detection(parking_bounding_rects, frame_gray, pk_status, parking_buffer, video_cur_pos, parking_data)

    # Parking overlay
    if config['parking_lot_overlay']:
        for ind, park in enumerate(parking_data):
            coors = np.array(park['coors'])
            if parking_lot_state[ind]:
                color = (0,255,0)
                spot = spot + 1
                array_of_free_spaces.append(ind)
            else:
                color = (0,0,255)
                occupied = occupied+1

            # Draw real rectangles
            cv2.drawContours(f_out, [coors], contourIdx=-1, color=color, thickness=2, lineType=cv2.LINE_8)

            takes = cv2.moments(coors)

            cent_id = (int(takes['m10']/takes['m00'])-3, int(takes['m01']/takes['m00'])+3)
            cv2.putText(f_out, str(park['id']), (cent_id[0]+1, cent_id[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(f_out, str(park['id']), (cent_id[0]-1, cent_id[1]-1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(f_out, str(park['id']), (cent_id[0]+1, cent_id[1]-1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(f_out, str(park['id']), (cent_id[0]-1, cent_id[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(f_out, str(park['id']), cent_id, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)

    # Display video
    cv2.imshow('Image processing project (Parking Lot)', f_out)
    cv2.waitKey(1)

    # Keyboard options
    keyboard_options(vv_current_frame, f_out)

    # Export reading in file (to reading this for API app)
    coordinates_generator(array_of_free_spaces)
    
        
cap.release()
cv2.destroyAllWindows()

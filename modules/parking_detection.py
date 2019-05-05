# contributors: Menna
# -------------------------------

import numpy as np
from modules.config import *

# Detect subtraction of frames
def parking_detection(parking_bounding_rects, f_gray, parking_lot_state, parking_buffer, video_cur_pos, parking_data):
	if config['parking_detection']:
	    for ind, park in enumerate(parking_data):
	        coors = np.array(park['coors'])
	        rect = parking_bounding_rects[ind]
	        roi_gray = f_gray[rect[1]:(rect[1]+rect[3]), rect[0]:(rect[0]+rect[2])] # crop roi for faster calculation
	        # print np.std(roi_gray)

	        coors[:,0] = coors[:,0] - rect[0] # shift contour to roi
	        coors[:,1] = coors[:,1] - rect[1]
	        # print np.std(roi_gray), np.mean(roi_gray)
	        status = np.std(roi_gray) < 22 and np.mean(roi_gray) > 53
	        # If detected a change in parking status, save the current time
	        if status != parking_lot_state[ind] and parking_buffer[ind]==None:
	            parking_buffer[ind] = video_cur_pos
	        # If status is still different than the one saved and counter is open
	        elif status != parking_lot_state[ind] and parking_buffer[ind]!=None:
	            if video_cur_pos - parking_buffer[ind] > config['park_sec_to_wait']:
	                parking_lot_state[ind] = status
	                parking_buffer[ind] = None
	        # If status is still same and counter is open
	        elif status == parking_lot_state[ind] and parking_buffer[ind]!=None:
	            #if video_cur_pos - parking_buffer[ind] > config['park_sec_to_wait']:
	            parking_buffer[ind] = None
	        # print(parking_lot_state)
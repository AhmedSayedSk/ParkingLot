# contributors: Marwa & Esmat
# -------------------------------

import cv2
from modules.config import *

# Set capture device or file
cap = cv2.VideoCapture(fn_ved)

video_info = {
	'fps':    cap.get(cv2.CAP_PROP_FPS),
  'width':  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
  'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
  'fourcc': cap.get(cv2.CAP_PROP_FOURCC),
  'num_of_frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
}

cap.set(cv2.CAP_PROP_POS_FRAMES, config['start_frame']) # jump to frame
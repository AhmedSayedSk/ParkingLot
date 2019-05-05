import argparse

# contributors: Ahmed Sayed
# -------------------------------

# Detect mode
parser = argparse.ArgumentParser(description='Parking lot')
parser.add_argument("--mode", dest="fn_test_mode", required=True)
parser = parser.parse_args()

# Test mode
fn_test_mode = parser.fn_test_mode

# Test videos
fn_ved = "datasets/videos/parking_" + fn_test_mode + ".mp4"

# Test Images
fn_img = "datasets/images/parking_" + fn_test_mode + ".png"

# Saving coordinates of user mouse clicks
fn_yaml = "datasets/parking_yaml.yml"

# Main project configuration
config = {
  'parking_lot_overlay': True,
  'parking_detection': True,
  'min_area_motion_contour': 60,
  'park_sec_to_wait': 3,
  'start_frame': 0
}
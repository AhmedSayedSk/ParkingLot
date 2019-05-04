# contributors: Ahmed Sayed
# -------------------------------

fn = "datasets/parking1.mp4"
fn_yaml = "datasets/parking1.yml"
fn_yaml2 = "datasets/parking2.yml"
fn_out = "datasets/output.avi"

config = {
	'save_video': False,
  'text_overlay': False,
  'parking_lot_overlay': True,
  'parking_id_overlay': False,
  'parking_detection': True,
  'min_area_motion_contour': 60,
  'park_sec_to_wait': 3,
  'start_frame': 0
}
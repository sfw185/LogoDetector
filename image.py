import os
import glob
import cleanup
import cv2 as cv

def detect_logos():
  logos = glob.glob('./input/logos/*.jpg')
  for logo in logos:
    print 'Testing against {0}'.format(logo)
    detect_logo(logo)

def detect_logo(logo_path):
  cleanup.delete_files('./output/*.jpg')
  frames = glob.glob('./input/frames/*.jpg')

  logo =  cv.imread(logo_path, 0)
  w, h = logo.shape[::-1]

  for frame_path in frames:
    frame = cv.imread(frame_path, 0)
    result = cv.matchTemplate(frame, logo, cv.TM_CCOEFF_NORMED)
    _, __, ___, top_left = cv.minMaxLoc(result)

    bottom_right = (top_left[0] + w, top_left[1] + h)
    img = cv.rectangle(frame, top_left, bottom_right, 255, 2)
    cv.imwrite('./output/{0}'.format(os.path.basename(frame_path)), img)

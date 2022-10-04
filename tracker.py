# Built off examples from openCV docs
# docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html


import numpy as np
import cv2

def bounding_box():
	cap = cv2.VideoCapture(0)

	while(True):
		# Capture frame by frame
		ret, frame = cap.read()
		frame = cv2.GaussianBlur(frame,(25,25),0)

		# Convert BGR to HSV
		HSVFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		BGRFrame = frame

		# Define range of orange in HSV/BGR
		lower_orangeBGR = np.array([106, 0, 255])
		higher_orangeBGR = np.array([21, 0, 255])
		lower_orangeHSV = np.array([162, 100, 100])
		higher_orangeHSV = np.array([182, 255, 255])

		# Threshold the images
		maskBGR = cv2.inRange(BGRFrame, lower_orangeBGR, higher_orangeBGR)
		maskHSV = cv2.inRange(HSVFrame, lower_orangeHSV, higher_orangeHSV)

		# Create RGB Bounding Rectangle
		x,y,w,h = cv2.boundingRect(maskBGR)
		cv2.rectangle(maskBGR, (x,y), (x+w, y+h), (0,255,0), 2)
		cv2.rectangle(BGRFrame, (x,y), (x+w, y+h), (0,255,0), 2)

		# Display the resulting frames
		cv2.imshow('BGRFrame',BGRFrame)
		cv2.imshow('maskBGR',maskBGR)

		# Create HSV Bounding Rectangle
		x,y,w,h = cv2.boundingRect(maskHSV)
		cv2.rectangle(maskHSV, (x,y), (x+w, y+h), (0,255,0), 2)
		cv2.rectangle(HSVFrame, (x,y), (x+w, y+h), (0,255,0), 2)

		# Display the resulting frames
		cv2.imshow('HSVFrame',HSVFrame)
		cv2.imshow('maskHSV',maskHSV)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release capture
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	bounding_box()


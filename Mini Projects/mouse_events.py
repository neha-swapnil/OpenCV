# importing libraries

import cv2
import numpy as np

# creating a black image and a new window

windowName = 'Drawing'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)

# mouse callback function

def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
	if event == cv2.EVENT_MBUTTONDOWN:
        	cv2.circle(img, (x, y), 20, (0, 0, 255), -1)
    	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img, (x, y), 30, (255, 0, ), -1)

# binding the callback function to window

cv2.setMouseCallback(windowName, draw_circle)

#main function

def main():

	while(True):
		cv2.imshow(windowName, img)
		if cv2.waitKey(20) == 27:
			break

	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

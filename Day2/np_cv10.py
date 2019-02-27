import cv2
import numpy as np

def main():

	img = np.zeros((512, 512, 3), np.uint8) #creating an image using a built-in function zeros (size= 512*512 , channels=3) 8-bit uint

	cv2.line(img, (0, 99), (99, 0), (255, 0, 0)) #line function 0-99 x1,y1 99-0 x2,y2 **** (255, 0, 0) color blue BGR

	cv2.rectangle(img, (40,60), (80,70), (0, 255, 0), 2) #2=thickness

	cv2.circle(img, (60,60), 10, (0, 0, 255), -1) #10=radius -1=fill

	cv2.ellipse(img, (160,260), (50, 20), 0, 0, 360, (127, 127, 127), -1)

	points = np.array([[80, 2], [125, 10], [179, 19],[250, 5],[30, 50]], np.int32)
	points = points.reshape((-1, 1, 2))
	cv2.polylines(img, [points], True, (0, 255, 255))

	text1 = 'Test Text'
	cv2.putText(img, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0))

	cv2.imshow('Demo', img)
	cv2.waitKey(0)
	cv2.destoryWindow('Demo')

if __name__ == "__main__":
	main()

import cv2
import numpy as np

def main():

	windowName = "Preview"
	cv2.namedWindow(windowName)
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False

	while ret:

		ret, frame = cap.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray, 50, 250, apertureSize=5, L2gradient=True)
		lines = cv2.HoughLines(edges, 1, np.pi/180, 200)#angle accuracy of an accumulator = np.pi/180
		if lines is not None:
			for rho, theta in lines[0]:
				a= np.cos(theta)
				b= np.sin(theta)
				x0 = a*rho
				y0 = b*rho
				pts1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
				pts2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a))) #converting polar coordinates to cartesian coordinates
				cv2.line(frame, pts1, pts2, (0, 255, 0), 3)#drawing the lines on the frame

		cv2.imshow(windowName, frame)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__ == "__main__":
	main()

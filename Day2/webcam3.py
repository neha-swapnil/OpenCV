import cv2

def main():

	windowName = 'Live Video Feed'
	cv2.namedWindow(windowName)
	cap = cv2.VideoCapture(0)

	print('Width : ' + str(cap.get(3)))
	print('Height : ' + str(cap.get(4)))

	cap.set(3, 400)#standard width = 1024
	cap.set(4, 300)#standard height = 768

	print('Width : ' + str(cap.get(3)))
	print('Height : ' + str(cap.get(4)))

	if cap.isOpened():
		ret, frame = cap.read() #return frame
	else:
		ret = False

	while ret:

		ret, frame = cap.read()
		img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow(windowName, frame)
		cv2.imshow("GRAY", img2)
		if cv2.waitKey(1) == 27:
			break

	cv2.destroyWindow(windowName)
	cap.release()

if __name__ == "__main__":
	main()

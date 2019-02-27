import cv2

def main():

	windowName = "Live Video Feed"
	cv2.namedWindow(windowName)
	cap = cv2.VideoCapture(0)

	filename = '/home/neha/Desktop/OpenCV/OUTPUT/'
	codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
	framerate = 30
	resolution = (640,480)
	VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)#syntax

	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False
	
	while ret:

		ret, frame = cap.read()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		VideoFileOutput.write(frame)
		cv2.imshow(windowName, frame)
		if cv2.waitKey(1) == 27:
			break

	cv2.destroyWindow(windowName)
	VideoFileOutput.release()
	cap.release()

if __name__ == "__main__":
	main()

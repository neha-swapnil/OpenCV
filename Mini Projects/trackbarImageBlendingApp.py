import cv2

def emptyFunction():
	pass

def main():

	path = "/home/neha/Desktop/jungkook"
	
	imgpath1 =  path + "/jk111.jpg"
	imgpath2 =  path + "/jk222.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

	windowName = "Transition Demo"
	cv2.namedWindow(windowName)

	cv2.createTrackbar('Alpha', windowName, 0, 10, emptyFunction)

	while(True):

		cv2.imshow(windowName, output)

		if cv2.waitKey(1) == 27:
			break

		alpha = cv2.getTrackbarPos('Alpha', windowName) / 1000
		beta = 1 - alpha
		output = cv2.addWeighted(img1, alpha, img2, beta, 0)

		print (alpha, beta)

	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

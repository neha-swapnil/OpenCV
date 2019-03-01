import cv2

def main():

	path = "/home/neha/Desktop/jungkook/jk4.jpg"
	img1 = cv2.imread(path, 1)

	#output = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
	#output = cv2.resize(img1, None, fx=1.5, fy=1, interpolation=cv2.INTER_CUBIC)
	#output = cv2.resize(img1, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
	#output = cv2.resize(img1, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
	#output = cv2.resize(img1, None, fx=0.5, fy=1.5, interpolation=cv2.INTER_AREA)
	output = cv2.resize(img1, None, fx=0.5, fy=1.5, interpolation=cv2.INTER_AREA)

	cv2.imshow('Output', output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

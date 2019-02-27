import cv2

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk13.jpg"
	img = cv2.imread(imgpath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	cv2.imshow('JK_Show', gray)
	cv2.waitKey(0)
	cv2.destroyWindow('JK_Show')

if __name__ == "__main__":
	main()

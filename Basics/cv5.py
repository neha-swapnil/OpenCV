import cv2

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk11.jpg"
	img = cv2.imread(imgpath, 0) #reading the image as a gray scale image

	outpath = "/home/neha/Desktop/jk11.jpg"

	cv2.imshow('JK2', img)
	cv2.imwrite(outpath, img)
	cv2.waitKey(0)
	cv2.destroyWindow('JK2')

if __name__ == "__main__":
	main()

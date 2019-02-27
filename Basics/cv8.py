import cv2

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk14.jpg"
	img = cv2.imread(imgpath, 1)

	print (type(img))
	print (img.dtype)
	print (img.shape)
	print (img.ndim)
	print (img.size)

	cv2.imshow('JK_kid', img)
	cv2.waitKey(0)
	cv2.destroyWindow('JK_kid')

if __name__ == "__main__":
	main()

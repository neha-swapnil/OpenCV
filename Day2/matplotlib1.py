import cv2
import matplotlib.pyplot as plt

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk15.jpg"
	img = cv2.imread(imgpath, 0)

	plt.imshow(img) #the imshow function doesn't know whether the image is gray or not.we need to define cmap='gray'
	plt.show()

	#cv2.imshow('JK', img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

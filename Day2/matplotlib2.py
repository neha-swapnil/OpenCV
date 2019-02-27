import cv2
import matplotlib.pyplot as plt

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk15.jpg"
	img = cv2.imread(imgpath, 0)

	plt.imshow(img, cmap='gray')
	plt.title("Gray cmap")
	plt.xticks([])
	plt.yticks([])
	plt.show()
	plt.imshow(img, cmap='Reds')
	plt.title("Reds cmap")
	plt.xticks([])
	plt.yticks([])
	plt.show()
	plt.imshow(img, cmap='Accent')
	plt.title("Accent cmap")
	plt.xticks([])
	plt.yticks([])
	plt.show()


	#cv2.imshow('JK', img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

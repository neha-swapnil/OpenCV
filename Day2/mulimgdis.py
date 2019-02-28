import cv2
import matplotlib.pyplot as plt

def main():

	path1 = "/home/neha/Desktop/jungkook/jk4.jpg"
	path2 = "/home/neha/Desktop/jungkook/jk12.png"

	img1 = cv2.imread(path1, 1)
	img2 = cv2.imread(path2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

	plt.subplot(1, 2, 1)
	plt.imshow(img1)
	plt.title('JK1')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(1, 2, 2)
	plt.imshow(img2)
	plt.title('JK2')
	plt.xticks([])
	plt.yticks([])

	plt.show()

if __name__ == "__main__":
	main()

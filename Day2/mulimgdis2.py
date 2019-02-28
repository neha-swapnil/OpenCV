import cv2
import matplotlib.pyplot as plt

def main():

	path1 = "/home/neha/Desktop/jungkook/jk4.jpg"
	path2 = "/home/neha/Desktop/jungkook/jk12.png"

	img1 = cv2.imread(path1, 1)
	img2 = cv2.imread(path2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

	titles = ['JK1', 'JK2']
	images = [img1, img2]

	for i in range(2):

		plt.subplot(1, 2, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])

	plt.show()

if __name__ == "__main__":
	main()

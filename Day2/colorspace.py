import cv2
import matplotlib.pyplot as plt

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk15.jpg"
	img = cv2.imread(imgpath, 1)
	img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	plt.imshow(img)
	plt.title("Color image BGR")
	plt.xticks([])
	plt.yticks([])
	plt.show()

	plt.imshow(img1)
	plt.title("Color image RGB")
	plt.xticks([])
	plt.yticks([])
	plt.show()


if __name__ == "__main__":
	main()

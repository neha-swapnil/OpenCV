import cv2
import matplotlib.pyplot as plt

def main():

	path1 = "/home/neha/Desktop/jungkook/jk111.jpg"
	path2 = "/home/neha/Desktop/jungkook/jk222.jpg"

	img1 = cv2.imread(path1, 1)
	img2 = cv2.imread(path2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	
	add = img1 + img2
	sub = img1 - img2
	mul = img1 * img2
	div = img1 / img2

	titles = ['JK1', 'JK2', 'Add', 'Sub', 'Mul', 'Div']
	images = [img1, img2, add, sub, mul, div]

	for i in range(6):

		plt.subplot(1, 6, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])

	plt.show()

if __name__ == "__main__":
	main()

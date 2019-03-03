import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/jungkook/jk1.jpg"
	img1 = cv2.imread(path, 1)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

	rows, columns, channels = img1.shape
	print (img1.shape)
	print (rows)
	print (columns)
	print (channels)

	T = np.float32([[1, 0, 50], [0, 1, -50]])
	print (T)

	output = cv2.warpAffine(img1, T, (columns, rows))

	

	plt.imshow(output)
	plt.title('Shifted Image')
	plt.show()

if __name__ == "__main__":
	main()

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/jungkook/jk20.png"
	img = cv2.imread(path, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	#k = np.array(([0, 0, 0], [0, 1, 0], [0, 0, 0]), np.float32) #kernel or the convolution matrix - identity matrix
	k = np.array(([1, 0, -1], [0, 0, 0], [-1, 0, 1]), np.float32)#edge detection
	#k = np.array(np.ones((3, 3), np.float32))
	k = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]), np.float32)
	print (k)
	print(type(k))

	output = cv2.filter2D(img, -1, k)

	plt.subplot(1, 2, 1)
	plt.imshow(img)
	plt.title('Original Image')

	plt.subplot(1, 2, 2)
	plt.imshow(output)
	plt.title('Filtered Image')

	plt.show()

if __name__ == "__main__":
	main()

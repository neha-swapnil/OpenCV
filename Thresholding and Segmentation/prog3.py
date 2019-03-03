#Otsu's Binarization

import cv2
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/OpenCV/images/moon-craters.jpg"
	img = cv2.imread(path, 0)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	block_size = 513 #stands for neighbourhood of pixels on which these algo would work
	constant = 2
	th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)#mean algo
	th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)#binary algo

	output = [img, th1, th2]
	titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']

	for i in range(3):
		plt.subplot(1, 3, i+1)
		plt.imshow(output[i], cmap='gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
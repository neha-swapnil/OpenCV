import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/jungkook/jk111.jpg"
	img = cv2.imread(path, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	rows, columns, channels = img.shape
	p = 0.05 #5% probability of noise

	output= np.zeros(img.shape, np.uint8)#creating a new black window

	for i in range(rows):
		for j in range(columns):
			r = random.random()
			if r < p/2:#0-p/2
				#pepper sprinkle(black)
				output[i][j] = [0, 0, 0]
			elif r < p:#p/2-p
				#salt sprinkle(white)
				output[i][j] = [255, 255, 255]
			else:
				#keeping the image the same
				output[i][j] = img[i][j]
	

	plt.imshow(output)
	plt.title('Image with Salt and Pepper noise')
	plt.show()

if __name__ == "__main__":
	main()

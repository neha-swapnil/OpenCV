#to remove salt and pepper noise

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

	noise = np.zeros(img.shape, np.uint8)#creating a new black window

	for i in range(rows):
		for j in range(columns):
			r = random.random()
			if r < p/2:#0-p/2
				#pepper sprinkle(black)
				noise[i][j] = [0, 0, 0]
			elif r < p:#p/2-p
				#salt sprinkle(white)
				noise[i][j] = [255, 255, 255]
			else:
				#keeping the image the same
				noise[i][j] = img[i][j]

	denoised = cv2.medianBlur(noise, 3)#3= 3x3 matrix, 5= 5x5 matrix

	output = [img, noise, denoised]
	titles = ['Original', 'Salt n Pepper Noise', 'Denoised']

	for i in range(3):
		plt.subplot(1, 3, i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()

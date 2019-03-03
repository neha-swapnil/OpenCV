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

	R = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 0.5)#45degree, 0.5 scaling
	print (R)

	output = cv2.warpAffine(img1, R, (columns, rows))

	

	plt.imshow(output)
	plt.title('Rotated Image')
	plt.show()

if __name__ == "__main__":
	main()

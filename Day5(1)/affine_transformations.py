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

	point1 = np.float32([[100, 100], [300, 100], [100, 300]])
	point2 = np.float32([[200, 150], [400, 150], [200, 400]])
	#non-colinear points
	A = cv2.getAffineTransform(point1, point2)
	#point1 is set of points in input image
	#point2 is set of points in output image
	print (A)

	output = cv2.warpAffine(img1, A, (columns, rows))

	

	plt.imshow(output)
	plt.title('Transformed Image')
	plt.show()

if __name__ == "__main__":
	main()

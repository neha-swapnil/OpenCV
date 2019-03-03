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

	point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
	point2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
	#non-colinear points
	P = cv2.getPerspectiveTransform(point1, point2)
	#point1 is set of points in input image
	#point2 is set of points in output image
	print (P)

	output = cv2.warpPerspective(img1, P, (700, 700))

	

	plt.imshow(output)
	plt.title('Perspective Image')
	plt.show()

if __name__ == "__main__":
	main()

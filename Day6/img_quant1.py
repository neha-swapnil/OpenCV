import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk6.jpg"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	#reshape the image first
	Z = img.reshape((-1, 1))
	#change uint8 to float32
	Z = np.float32(Z)
	#criteria for clustering
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	#to find the k means cluster representation with just 2 colors
	K = 2
	#output1111
	ret, label1, center1 = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)#ret=true/false////labels////centers
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]

	output1 = res1.reshape((img.shape))

	#output2222
	K = 4
	ret, label1, center1 = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)#ret=true/false////labels////centers
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]

	output2 = res1.reshape((img.shape))

	#output3333
	K = 6
	ret, label1, center1 = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)#ret=true/false////labels////centers
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]

	output3 = res1.reshape((img.shape))
	output3 = img

	output = [img, output1, output2, output3]
	titles = ['Original', 'K=2', 'TELEA', 'NS']

	for i in range(4):
		plt.subplot(2, 2, i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()

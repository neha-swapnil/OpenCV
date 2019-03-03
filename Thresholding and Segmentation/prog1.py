import cv2
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/OpenCV/images/gray21.512.png"
	img = cv2.imread(path, 1)
	#img = cv2.cvtColor()
	th = 127
	max_val = 255
	ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
	ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)
	ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO)
	ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV)
	ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC)

	output = [img, o1, o2, o3, o4, o5]
	titles = ['Original', 'Binary', 'Binary Inv', 'ToZero', 'ToZero Inv', 'Trunc']

	for i in range(6):
		plt.subplot(2, 3, i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()

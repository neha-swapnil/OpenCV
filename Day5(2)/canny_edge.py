import cv2
import matplotlib.pyplot as plt

def main():

	path = "/home/neha/Desktop/jungkook/jk111.jpg"
	img = cv2.imread(path, 0)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	L1 = cv2.Canny(img, 100, 150, L2gradient= False)
	L2 = cv2.Canny(img, 150, 150, L2gradient= True)
	output = [img, L1, L2]
	titles = ['Original', 'L1 image', 'L2 image']

	for i in range(3):
		plt.subplot(1, 3, i+1)
		plt.imshow(output[i], cmap='gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()

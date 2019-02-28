import cv2
import matplotlib.pyplot as plt

def main():
    
	path = "/home/neha/Desktop/jungkook"
	imgpath1 =  path + "/jk111.jpg"
	imgpath2 =  path + "/jk222.jpg"
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	alpha = 0.5
	beta = 0.5
	gamma = 0
	#to achieve blending effect alpha+beta=1 (should satisfy)
	output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    #addWeighted()-> represents composite arithmetic operations
	#output = img1*alpha + img2*beta + gamma
	titles = ['JK1', 'JK2', 'Weighted Addition']
	images = [img1, img2, output]

	for i in range(3):
		plt.subplot(1, 3, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()

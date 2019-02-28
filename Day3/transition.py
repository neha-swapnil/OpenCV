import cv2
import numpy as np
import time

def main():
    
	path = "/home/neha/Desktop/jungkook"
	
	imgpath1 =  path + "/jk111.jpg"
	imgpath2 =  path + "/jk222.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	for i in np.linspace(0, 1, 100):
		alpha = i
		beta = 1 - alpha
		output = cv2.addWeighted(img1, alpha, img2, beta, 0)
		cv2.imshow('Transition', output)
		time.sleep(0.02)
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

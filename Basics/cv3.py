import cv2

def main():

	imgpath = "/home/neha/Desktop/jungkook/jk1.jpg"
	img = cv2.imread(imgpath)

	cv2.imshow('First', img)
	cv2.waitKey(0) #to bind the keyboard event with cv2.imshow() event 
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()

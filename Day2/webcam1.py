import cv2
import matplotlib.pyplot as plt

def main():

	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read() #return frame
		print (ret)
		print (frame)
	else:
		ret = False

	img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	plt.imshow(img)
	plt.title('Color Image RGB')
	plt.xticks([])
	plt.yticks([])
	plt.show()

	cap.release()

if __name__ == "__main__":
	main()

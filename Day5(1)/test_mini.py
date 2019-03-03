import cv2
import time

def main():

	path = "/home/neha/Desktop/jungkook/jk1.jpg"
	img1 = cv2.imread(path, 1)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

	rows, columns, channels = img1.shape
	print (img1.shape)
	print (rows)
	print (columns)
	print (channels)

	angle = 0 #360 clockwise

	while True:

		if angle == 360:#0 clockwise
			angle = 0
		R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 1) #divided by 2 is center pivot for rotation
		print (R)

		output = cv2.warpAffine(img1, R, (columns, rows))

		cv2.imshow('Rotated Image', output)
		angle = angle + 1
		time.sleep(0.01)

		if cv2.waitKey(1) == 27:
			break

#algo:-
#while true:
#	display image rotated with angle
#	angle++
#	if angle == 360
#		angle = 0

	cv2.destroyWindow('Rotated Image')


if __name__ == "__main__":
	main()

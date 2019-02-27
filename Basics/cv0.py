import cv2

img = cv2.imread("/home/neha/Pictures/Wallpapers/Firefox_wallpaper.png")

while True:
	cv2.imshow('frame',img)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()

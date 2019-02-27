#importing libraries

import cv2
import numpy as np

#empty function

def emptyFunction():
    pass

#main function

def main():
    
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)
    
    while(True):
        cv2.imshow(windowName, img1)
        
        if cv2.waitKey(1) == 27:
	    #escape key code 27
            break
        
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        
        img1[:] = [blue, green, red]
        print (blue, green, red)
        
cv2.destroyAllWindows()


#calling main()

if __name__ == "__main__":
	main()

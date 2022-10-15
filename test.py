import cv2
if __name__=='__main__':
    print("Test")
    while(True):
        cam = cv2.VideoCapture(0)
        cam.isOpened()
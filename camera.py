import cv2

vid  = cv2.VideoCapture(0)
if (vid.isOpened() == False):
    print("UNABLE TO READ FROM THE FEED")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while (True):
    ret , frame = vid.read()
    cv2.imshow("web cam" , frame)
    if cv2.waitKey(1) == 32:
        break 

vid.release()
cv2.destroyAllWindows()
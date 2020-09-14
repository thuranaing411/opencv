import cv2

# Opens the Video file
cap = cv2.VideoCapture('thura naing.mp4')
i = 0
while (cap.isOpened()):
    ret, p1 = cap.read()
    if ret == False:
        break
    cv2.imwrite('naing' + str(i) + '.jpg', p1)
    i += 1

cap.release()
cv2.destroyAllWindows()
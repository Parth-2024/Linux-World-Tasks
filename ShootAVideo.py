import cv2
cap=cv2.VideoCapture(1)
while True:
    status,photo=cap.read()
    cv2.imshow("My video",photo)
    if cv2.waitKey(8)==13:
        break
cv2.destroyAllWindows()
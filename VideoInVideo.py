import cv2
cap=cv2.VideoCapture(1)
cap2=cv2.VideoCapture(2)
while True:
    status1,photo1=cap.read()
    status2,photo2=cap2.read()
    crp=photo2[75:250,280:420]
    photo1[0:175,0:140]=crp
    cv2.imshow("My Video",photo1)
    if cv2.waitKey(8)==13:
        break
cv2.destroyAllWindows()
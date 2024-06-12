import cv2
cap=cv2.VideoCapture(2)
status,photo=cap.read()
face_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
lst=face_model.detectMultiScale(photo)
if len(lst)==0:
    print("No face")
else:
    x1=lst[0][0]
    y1=lst[0][1]
    x2=x1+lst[0][2]
    y2=y1+lst[0][3]
    cv2.imshow("My",photo[y1:y2,x1:x2])
    cv2.waitKey()
    cv2.destroyAllWindows()
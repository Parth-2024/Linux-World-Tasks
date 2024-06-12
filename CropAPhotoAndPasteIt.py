import cv2
cap=cv2.VideoCapture(2)
status,photo=cap.read()
face_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
crp=face_model.detectMultiScale(photo)
if len(crp)==0:
    print("No Face Detected")
else:
    x1=crp[0][0]
    y1=crp[0][1]
    x2=x1+crp[0][2]
    y2=y1+crp[0][3]
    crop=photo[y1:y2,x1:x2]
    photo[0:crp[0][3],0:crp[0][2]]=crop
    cv2.imwrite("Crp.png",photo)
    cv2.imshow("Photo in Photo",photo)
    cv2.waitKey()
    cv2.destroyAllWindows()

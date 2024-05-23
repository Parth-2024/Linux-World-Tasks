import cv2
cap1=cv2.VideoCapture(1)
cap2=cv2.VideoCapture(2)
status1,photo1=cap1.read()
status2,photo2=cap2.read()
print(photo1.shape)
print(photo2.shape)
photo2[0:480,320:640]=photo1[0:480,0:320]
cv2.imwrite("Collage.png",photo2)
cv2.imshow("Collage",photo2)
cv2.waitKey()
cv2.destroyAllWindows()
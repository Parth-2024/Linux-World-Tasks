import cv2
cap=cv2.VideoCapture(1)
status,photo=cap.read()
cv2.imwrite("Nayan.png",photo)
cv2.imshow("Nayan",photo)
print(photo)
cv2.waitKey()
cv2.destroyAllWindows()
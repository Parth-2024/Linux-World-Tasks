import cv2
photo=cv2.imread("Nayan.png")
print(photo.shape)
crpPhoto=photo[100:300,250:420]
photo[0:200,0:170]=crpPhoto
cv2.imwrite("Crp.png",photo)
cv2.imshow("Parth",photo)
cv2.waitKey()
cv2.destroyAllWindows()
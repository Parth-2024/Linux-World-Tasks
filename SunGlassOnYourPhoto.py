import cv2
photo=cv2.imread("Nayan.png")
shades=cv2.imread("662854bd124a854eb7277247-wearme-pro-flat-top-polarized-lens-removebg-preview.png")
# shades=cv2.imread("360_F_268003032_PYDU5gcLWsTAFSN2mnYO2CN8fw1dUBBj-removebg-preview.png")
print(shades.shape)
print(photo.shape)
shd1=shades[2:35,0:48]
shd2=shades[2:10,49:56]
shd3=shades[2:35,57:100]
photo[227:260,300:348]=shd1
photo[227:235,348:355]=shd2
photo[227:260,355:398]=shd3
print(type(photo))
#for second set of shades
# shd1=shades[11:44,8:48]
# shd2=shades[12:25,45:54]
# shd3=shades[11:44,53:93]
# photo[227:260,305:345]=shd1
# photo[228:241,344:353]=shd2
# photo[227:260,353:393]=shd3
print(photo)
cv2.imwrite("Yoo2.png",photo)
cv2.imwrite("Yoo.png",photo)
cv2.imshow("Yoo",photo)
cv2.waitKey()
cv2.destroyAllWindows()

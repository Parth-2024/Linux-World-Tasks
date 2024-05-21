import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
image=[]
for i in range(1,76):
    for j in range(1,151):
        image.append([230,0,0])
for i in range(76,151):
    for j in range(1,41):
        image.append([0,230,0])
    for k in range(41,151):
        image.append([0,0,230])
# for i in range(91,111):
#     for j in range(46,61):
#         image.append([0,0,0])
#     for j in range(61,81):
#         image.append([0,0,230])
#     for j in range(81,111):
#         image.append([0,0,0])
#     for j in range(111,131):
#         image.append([0,0,230])
#     for j in range(131,151):
#         image.append([0,0,0])
# for i in range(111,151):
#     for j in range(1,151):
#         image.append([0,0,0])
print(image)
image=np.array(image,dtype=np.uint8)
image=image.reshape(150,150,3)
image[81:101,71:91]=[0,0,0]
image[81:101,121:141]=[0,0,0]
image[121:151,96:116]=[0,0,0]
image[76:151,61:66]=[0,0,0]
# image[121:151,42:60]=[0,0,0]
print(image)
print(type(image))
print(image.shape)
cv2.imshow("pixel-art",image)
cv2.waitKey(50000)
cv2.destroyAllWindows()
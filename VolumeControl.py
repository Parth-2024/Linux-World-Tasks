import cv2,time
import numpy as np
import cv2
import cvzone
import cvzone.FPS
from cvzone.HandTrackingModule import HandDetector
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume)) 
volRange=volume.GetVolumeRange()
volMin=volRange[0]
volMax=volRange[1]
cap=cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS,60)#sets the fps of the camera
cap.set(3,640)
cap.set(4,480)
fpsReader=cvzone.FPS.FPS(avgCount=30)
detector=HandDetector(staticMode=False,maxHands=2,modelComplexity=1,detectionCon=0.7,minTrackCon=0.5)
volBar=400
vol=0
while True:
    status,img=cap.read()
    fps,img=fpsReader.update(img,pos=(20,50),bgColor=(255,255,0),textColor=(200,0,0),scale=2,thickness=2)#for customization
    hands,img=detector.findHands(img,draw=True,flipType=True)
    if hands:
        #information for the first hand detected
        hand1=hands[0] #Get the first hand detected
        lmList1=hand1['lmList']#(x,y,z)list of 21 landmarks for the first hand
        bbox1=hand1["bbox"] #bounding box around the first hand
        center1=hand1["center"]#center corrdinates of the first hand
        handType1=hand1["type"] #type of the first hand("Left" or "Right")

        fingers1=detector.fingersUp(hand1)
        print(f"H1={fingers1.count(1)}",end=" ")#Prints the count of the fingers that are up
        tipOfIndexFinger1=lmList1[8][0:2]
        tipOfthumb1=lmList1[4][0:2]
        #Calculate distance between specific landmarks on the first hand and  draw it on the image
        length,info,img=detector.findDistance(tipOfIndexFinger1,tipOfthumb1,img,color=(255,255,0),scale=5)
        print(length)
        vol=np.interp(length,[10,140],[volMin,volMax])
        volBar=np.interp(length,[10,140],[400,150])
        volPer=np.interp(length,[10,140],[0,100])
        volume.SetMasterVolumeLevel(vol, None)
        cv2.rectangle(img,(50,150),(85,400),(255,0,255),3)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(255,0,255),cv2.FILLED)
        cvzone.putTextRect(img, f"{int(volPer)}%", (40,450), scale=1, thickness=3, colorT=(0, 0, 255),
                colorR=(255, 255, 0), font=cv2.FONT_HERSHEY_COMPLEX,
                offset=10, border=5, colorB=(200, 0, 0))
        print(" ")#New line for better readability #her lmList[the point for our finger's tip][0:2 gives x and y point]
    cv2.imshow("Image",img)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
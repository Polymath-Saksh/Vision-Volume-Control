import cv2
import time
import numpy as np
import math
import HandTrackModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#############################################
wcam,hcam = 640,480

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol,maxVol = volRange[0],volRange[1]
vol = 0
volBar = 400
#volume.SetMasterVolumeLevel(-20.0, None)
#############################################

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
detector = htm.HandDetector(detectionCon=0.75)
pTime = 0
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw = False)
    #Extract the tip of the index and thumb fingers
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),15,(255,0,40),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,40),cv2.FILLED)
        
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

        length = math.hypot(x2-x1,y2-y1)
        if length<50:
            cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
        else:
            cv2.circle(img,(cx,cy),15,(255,40,40),cv2.FILLED)
        #Hand range 50-300
        #Volume Range -65 - 0
        vol = np.interp(length,[50,300],[minVol,maxVol])
        volBar = np.interp(length,[50,300],[400,150])
        volume.SetMasterVolumeLevel(vol, None)

        cv2.rectangle(img,(50,150),(85,400),(0,255,0),2)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
        volPer = np.interp(vol,[minVol,maxVol],[0,100])
        cv2.putText(img,f'{int(volPer)} %',(40,450),
        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)

        print(length)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',
    (40,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2) 

    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
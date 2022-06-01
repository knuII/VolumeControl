import cv2
import time
import numpy as np
import HandTrackingModule as hTracker
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# width and height of cam
wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = hTracker.handDetector(DetectionConf=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
    #volume.GetMasterVolumeLevel()
VolRange = volume.GetVolumeRange()

minVol = VolRange[0]
maxVol = VolRange[1]
vol = 0
volBar = 400
length = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2)//2, (y1 + y2)//2
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 2)

        length = math.hypot(x2 - x1, y2 - y1)
        #print(length)

        #Range of Pixels for Hand = 50 to 300
        #Range of values (pycaw) for volume = -65 to 0
        #To covert, we use numpy

        vol = np.interp(length, [50, 200], [minVol, maxVol])
        #print (vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length <50:
            cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)
    volBar = np.interp(length, [50, 200], [400, 150])
    cv2.rectangle(img, (50,150), (85,400), (0,255,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    #FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 2)


    cv2.imshow("IMG", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == ord("k"):
        break

cap.release()
cv2.destroyAllWindows()
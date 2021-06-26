import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

pTime = 0
cTime = 0
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPositions(img, draw = False)
    print(lmlist)

    if len(lmlist) != 0:
        dist = int(math.sqrt((lmlist[8][0] - lmlist[4][0])**2 + (lmlist[8][1] - lmlist[4][1])**2))
        lc_x, lc_y = (lmlist[8][0] + lmlist[4][0])//2, (lmlist[8][1] + lmlist[4][1])//2

        cv2.circle(img, (lmlist[4][0], lmlist[4][1]), 8, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[8][0], lmlist[8][1]), 8, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (lc_x, lc_y), 8, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (lmlist[4][0], lmlist[4][1]), (lmlist[8][0], lmlist[8][1]), (255, 0, 0), 3)

        vol = np.interp(dist, [50,250], [minVol,maxVol])
        volBar = np.interp(dist, [50,250], [400, 150])
        volPer = np.interp(dist, [50,250], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)

        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{str(int(volPer))}%' , (40, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 0, 0), 2)

        if dist < 50:
            cv2.circle(img, (lc_x, lc_y), 8, (0, 255, 0), cv2.FILLED)


    cv2.putText(img, f'Volume Control', (350, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
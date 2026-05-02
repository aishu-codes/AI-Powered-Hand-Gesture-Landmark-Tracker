import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# 1. Audio System Setup
devices = AudioUtilities.GetSpeakers()
# Fixed Audio Initialization
devices = AudioUtilities.GetSpeakers()
# Instead of devices.Activate, use device.EndpointVolume directly for newer versions
volume = devices.EndpointVolume.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange() 
minVol = volRange[0]
maxVol = volRange[1]

# 2. Hand Tracking Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Large Width
cap.set(4, 720)  # Large Height

print("Move your Thumb and Index finger to control volume. Press 'q' to quit.")

while cap.isOpened():
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(hand_lms.landmark):
                h, w, c = img.shape
                # Calculate exact pixel coordinates
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            # Logic to control volume using Finger IDs 4 (Thumb) and 8 (Index)
            if len(lmList) >= 21:
                x1, y1 = lmList[4][1], lmList[4][2] # Thumb
                x2, y2 = lmList[8][1], lmList[8][2] # Index
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                # Draw tracking circles and line
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Calculate distance between fingers
                length = math.hypot(x2 - x1, y2 - y1)

                # Map finger distance to volume
                vol = np.interp(length, [50, 300], [minVol, maxVol])
                volBar = np.interp(length, [50, 300], [400, 150])
                volPer = np.interp(length, [50, 300], [0, 100])

                volume.SetMasterVolumeLevel(vol, None)

                # Visual Volume UI
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

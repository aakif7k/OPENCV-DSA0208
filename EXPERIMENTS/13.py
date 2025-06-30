# 13. Perform Perspective Transformation on the Video

import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1, pts2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    dst = cv2.warpPerspective(frame, M, (300, 300))
    cv2.imshow("Perspective Video", dst)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

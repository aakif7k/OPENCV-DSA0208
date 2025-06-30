import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
gradient = cv2.magnitude(sobelx, sobely)

cv2.imshow("Gradient Mask", gradient.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

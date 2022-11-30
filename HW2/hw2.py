# -*- coding: utf-8 -*-
"""HW2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N861QTLi00wvB3dvewXR-Lhcn1bWEaLH
"""

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img1 = cv2.imread("img1.png")

ret, corners = cv2.findChessboardCorners(img1, (24, 17), None)

print(corners)

gray = cv2.cvtColor(img1 ,cv2.COLOR_BGR2GRAY)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

final_pic = cv2.drawChessboardCorners(img1, (24,17), corners2, ret)

cv2_imshow(final_pic)

cv2.imwrite('4_3.png', final_pic)

objectP = np.zeros((24*17,3), np.float32)
objectP[:,:2] = np.mgrid[0:24,0:17].T.reshape(-1,2)
objectPoints = []
imagePoints = []
imagePoints.append(corners2)
objectPoints.append(objectP)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objectPoints, imagePoints, img1.shape[1::-1], None, None)
print('ret =', ret)
print('camera matrix =' , mtx)
print('dist coefficience =' , dist)
print('rotation vectors =' , rvecs)
print('translation vectors =' , tvecs)

print('k1 =', dist[0][0])
print('k2 =', dist[0][1])
print('k3 =', dist[0][4])
print('p1 =', dist[0][2])
print('p2 =', dist[0][3])

img5 = cv2.imread('img5.png')
cv2_imshow(img5)

newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, img5.shape[1::-1], 0, img5.shape[1::-1])

dst = cv2.undistort(img5, mtx, dist, None, newcameramtx)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2_imshow(dst)
cv2.imwrite('4_6.png', dst)

img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
img3 = cv2.imread('img3.png')
img4 = cv2.imread('img4.png')
img5 = cv2.imread('img5.png')
images = [img1, img2, img3, img4]

objPoints = []
imgPoints = []
objectP2 = np.zeros((17*24,3), np.float32)
objectP2[:,:2] = np.mgrid[0:17,0:24].T.reshape(-1,2)

for image in images:
    ret, corners = cv2.findChessboardCorners(image, (24,17))
    if ret == True:
        objPoints.append(objectP)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgPoints.append(corners2)

ret, corners = cv2.findChessboardCorners(img2, (17,24))

objPoints.append(objectP2)
gray = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
imgPoints.append(corners2)

ret2, mtx3, dist2, rvecs2, tvecs2 = cv2.calibrateCamera(objPoints, imgPoints, img1.shape[1::-1], None, None)

mtx4, roi = cv2.getOptimalNewCameraMatrix(mtx3, dist2, img1.shape[1::-1], 0, img1.shape[1::-1])

dst = cv2.undistort(img5, mtx3, dist2, None, mtx4)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2_imshow(dst)
cv2.imwrite('4_7.png', dst)

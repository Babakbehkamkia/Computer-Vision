# -*- coding: utf-8 -*-
"""HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ax8flWlhRiTd2V6DGb8sN9Cx2oBm7VTW
"""

import cv2
from google.colab.patches import cv2_imshow
cv2.__version__

img_BGR = cv2.imread("background.png")

img_RGB = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2RGB)

cv2_imshow(img_BGR)

cv2_imshow(img_RGB)

small_img = cv2.resize(img_RGB, (570, 290))
cv2_imshow(small_img)

first = cv2.line(small_img, (10,10), (560,10), (255,0,0), 3) 
second = cv2.line(first, (10,10), (10, 280), (255,0,0), 3) 
third = cv2.line(second, (560, 280), (560,10), (255,0,0), 3) 
final = cv2.line(third, (10,280), (560, 280), (255,0,0), 3) 
cv2_imshow(final)

first_circle = cv2.circle(final, (10,10), 3, (0,0,255), 3)
second_circle = cv2.circle(first_circle, (10,280), 3, (0,255,0), 3)
third_circle = cv2.circle(second_circle, (560,10), 3, (100,10,100), 3)
final_circle = cv2.circle(third_circle, (560,280), 3, (50,100,150), 3)
cv2_imshow(final_circle)

"""# end.png"""

start = cv2.resize(img_RGB, (570, 290))
cv2_imshow(start)

step1 = cv2.line(start, (10,10), (560,10), (0,0,0), 1) 
step1 = cv2.line(step1, (10,10), (10,280), (0,0,0), 1) 
cv2_imshow(step1)

step2 = step1
for i in range(1,8):
    step2 = cv2.line(step2, (10,10), (i*80,140), (0,0,0), 1) 
    step2 = cv2.line(step2, (i*80,140), (10,280), (0,0,0), 1) 
cv2_imshow(step2)

step3 = step2
for i in range(0,7):
    step3 = cv2.line(step3, (560,10), (i*80,140), (0,0,0), 1) 
    step3 = cv2.line(step3, (i*80,140), (560,280), (0,0,0), 1) 
cv2_imshow(step3)

cv2.imwrite("mypic.jpg",step3)
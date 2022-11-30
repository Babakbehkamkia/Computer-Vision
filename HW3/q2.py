# -*- coding: utf-8 -*-
"""Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ty9PREh3j3rr-OwIoLEr4_AcHF74Rp7U
"""

# Import Your Libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

"""## Part 1

### Your Histogram Equalization Function
"""

def hist_equ(image):
    '''
    input:
    image (ndarray): input image
    output:
    output_image (ndarray): enhanced image
    '''
    
    ############
    # Your code
    # Start

    values, counts = np.unique(image, return_counts=True)
    cumulative = np.cumsum(counts, axis=0)
    # print(cumulative)
    cumulative = cumulative / (image.shape[0] * image.shape[1])

    cumulative = list(map(int, 255 * cumulative))

    mapping = []
    previous_val = 0
    for i in range(256):
      if i in values:
        previous_val = cumulative[np.where(values == i)[0][0]]
      mapping.append(previous_val)
          
    # print(mapping)
    # print(len(cumulative))
    # print(image.shape)
    # print(values.shape)

    output_image=np.zeros_like(image)

    for i in range(len(image)):
      for j in range(len(image[0])):
        output_image[i,j]=mapping[image[i,j]]
    # End
    
    return output_image

img = cv2.imread('River.jpg', 0)

### YOUR CODE ###
# START
equ = hist_equ(img)
# END

res = np.hstack((img, equ)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')

"""### Histogram Equalization OpenCV Library"""

img = cv2.imread('River.jpg', 0)

### YOUR CODE ###
# START
equ = cv2.equalizeHist(img)
# END

res = np.hstack((img, equ)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')

"""## Part 2

### CLAHE OpenCV Library
"""

def CLAHE(image, gridSize, clip_limit):
    '''
    inputs:
    image (ndarray): input image
    gridSize (tuple): window size
    clip_limit (int): threshold for contrast limiting
    output:
    output_image (ndarray): improved image
    '''

    ############
    # Your code
    # Start
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=gridSize)
    output_image = clahe.apply(image)
    # End

    return output_image

img = cv2.imread('River.jpg', 0)

### YOUR CODE ###
# START
clh = CLAHE(img, (5, 5), 3.0)
# END

res = np.hstack((img, clh)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')

"""## Part 3
Repeat for City image
"""

img = cv2.imread('city.jpg', 0)

### YOUR CODE ###
# START
equ = hist_equ(img)
# END

res = np.hstack((img, equ)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')

# ========================================

img = cv2.imread('city.jpg', 0)

### YOUR CODE ###
# START
equ = cv2.equalizeHist(img)
# END

res = np.hstack((img, equ)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')

# ========================================


img = cv2.imread('city.jpg', 0)

### YOUR CODE ###
# START
clh = CLAHE(img, (5, 5), 3.0)
# END

res = np.hstack((img, clh)) #stacking images side-by-side

plt.figure(figsize=(16, 16))
plt.imshow(res, cmap='gray')
# -*- coding: utf-8 -*-
"""HW4_org.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YLV8BrJ8HxuRw-45Y7HCna3pNzPX63t6
"""

from google.colab import drive
drive.mount('/content/drive')

path = "/content/drive/My Drive/CV_course/HW4/"

"""# Setup"""

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import fft

"""# Q3

## Part A

Complete the implementation for the following function using basic operations only.
Note that the point of this problem is for you to understand how convolution works. We don't care about optimality.
"""

def filter_2d(image, kernel):
    """
    Convolves an image with the kernel, applying zero-padding to maintain the size of the image.

    Parameters
    ----------
    image: ndarray
        2D array, representing a grayscale image.
    kernel: ndarray
        2D array, representing a linear kernel.
    Returns
    -------
    ndarray
        The result of convolving `image` with `kernel`.
    """
    result = cv2.filter2D(image,-1,kernel)
    return result

"""## Part B

Complete the implementation for the following function.
"""

def averaging_kernel(size):
    """
    Returns an averaging kernel with the specified size.

    Parameters
    ----------
    size: int
        Width and height of the kernel.

    Returns
    -------
    ndarray
        The averaging kernel.
    """
    result = np.ones((size,size))
    result /= (size**2)
    return result

"""Using the function you have just defined, try to smooth out the noise in the following image.
Try out various window sizes and analyze the results.
"""

im = cv2.imread(path + 'Q3/salt_and_pepper_low.jpeg')
plt.imshow(im)
plt.axis('off')

kernel = averaging_kernel(3)
im_smoothed = filter_2d(im, kernel)
plt.imshow(im_smoothed)
plt.axis('off')

"""## Part C

An averaging filter isn't enough for the next image you have to deal with. Instead, modify your implementation for `filter_2d` to instead calculate the non-linear **median** filter and try to smooth out this image.
You are encouraged to try out different kernel sizes.
"""

def median_filter(image, size):
    """
    Applies the median filter to the image with the given window size.

    Parameters
    ----------
    image: ndarray
        2D array, representing a grayscale image.
    size: int
        Size of the window for median calculation.
    Returns
    -------
    ndarray
        The result of convolving `image` with `kernel`.
    """
    result = cv2.medianBlur(image,size)
    return result

im = cv2.imread(path + 'Q3/salt_and_pepper_high.jpeg')
plt.imshow(im)
plt.axis('off')

im_smoothed = median_filter(im, size=5)
plt.imshow(im_smoothed)
plt.axis('off')

"""## Part D

Based on the equation presented for the derivative of an image in slide 18, create a 3x3 filter to calculate it using `filter_2d`.

*Hint*: Focus on the derivative along one of the axis only. There will just be 2 non-zero elements in the kernel.

"""

derivative_kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])

########################
# Your code goes here. #
########################

"""Apply this kernel to the following image. Can we somehow reduce the effect of noise on the result?"""

im = cv2.imread(path + 'Q3/cameraman_noisy.png')
plt.imshow(im)
plt.axis('off')

im_smoothed = filter_2d(im, derivative_kernel)
plt.imshow(im_smoothed)
plt.axis('off')

"""#Q4"""

def psnr(original, noisy):
    """
    Calculating Peak signal to noise ratio.

    ----------
    parameters:
        original : numpy 2D array, representing a original image.
        noisy : numpy 2D array, representing a noisy image.
    
    return:
        PSNR value
    """
    mse = np.mean((original - noisy) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    psnr_value = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return psnr_value

def denoise_image(image):
    """
    Denoises the input image.
    ----------
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result denoised image.   
    """

    fourier = fft.fft2(image)
    shifted_f = fft.fftshift(np.abs(fourier))

    plt.imshow(shifted_f,cmap='gray')
    plt.show()

    size = image.shape
    shifted_f[int(size[0]/2) - 25: int(size[0]/2) + 25, int(size[1]/2) - 25: int(size[1]/2) + 25] = 0
    m = np.max(shifted_f)
    shifted_f /= m
    peaks1 = shifted_f < 0.005
    
    peaks1 = fft.ifftshift(peaks1)
    denoised = fourier * peaks1
    denoised = np.real(fft.ifft2(denoised))
    return denoised

def f(x,y):
  return np.sin((1/2)*np.pi*x)+np.cos((1/3)*np.pi*y)

original_image = cv2.imread(path + "Q4/original_image.png",0)

X,Y = original_image.shape
noise = np.zeros((X,Y))
for i in range(X):
  for j in range(Y):
    noise[i,j] = f(i,j)*100

noisy_image = original_image + noise

plt.imshow(noisy_image,cmap='gray')
plt.show()

denoised_image = denoise_image(noisy_image)

plt.imshow(denoised_image, cmap='gray')
plt.show()

print("PSNR between noisy image and original image = ",
      psnr(original_image,noisy_image))
print("PSNR between denoised image and original image = ",
      psnr(original_image,denoised_image))


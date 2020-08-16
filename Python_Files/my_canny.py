import cv2
import numpy as np
import time
from scipy import ndimage
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import matplotlib.pyplot as plt

def gaussian_kernel(size, sigma=1.8):
    size = int(size) // 2   # c1 * 1
    x, y = np.mgrid[-size:size + 1, -size:size + 1]     # c2 * 1
    normal = 1 / (2.0 * np.pi * sigma ** 2)     # c3 * 1
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal      # c4 * 1

    return g

def gaussian_blur(img):
    blur = cv2.GaussianBlur(img, (5, 5), 1.4)

    return blur

def sobel_filter(img):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)     #c5 * 1
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)     #c5 * 1

    Ix = ndimage.filters.convolve(img, Gx).astype(float)    # c6 * 1
    Iy = ndimage.filters.convolve(img, Gy).astype(float)    # c6 * 1

    G = np.hypot(Ix, Iy)    # c7 * 1
    G = G / G.max() * 255   # c8 * 1
    theta = np.arctan(Iy, Ix)   # c9 * 1

    return G, theta

def non_max_suppression(img, D):
    M, N = img.shape    # c10 * 1
    Z = np.zeros((img.shape))    # c11 * 1
    angle = D * 180. / np.pi    # c12 * 1
    angle[angle < 0] += 180     # c13 * 1

    for i in range(1, M - 1):   # c14 * M - 2
        for j in range(1, N - 1):   # c15 * ((M - 2) * (N - 2))
            if img[i, j] != 0:
                try:    # c16 * ((M - 2) * (N - 2))
                    q = 255     # c17 * ((M - 2) * (N - 2))
                    r = 255     # c17 * ((M - 2) * (N - 2))

                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):  # c18 * ((M - 2) * (N - 2))
                        q = img[i, j + 1]   # c19 * A0
                        r = img[i, j - 1]   # c19 * A0
                    # angle 45
                    elif 22.5 <= angle[i, j] < 67.5:    # c20 * (((M - 2) * (N - 2)) - A0)
                        q = img[i + 1, j - 1]   # c19 * A45
                        r = img[i - 1, j + 1]   # c19 * A45
                    # angle 90
                    elif 67.5 <= angle[i, j] < 112.5:   # c20 * (((M - 2) * (N - 2)) - A0 - A45)
                        q = img[i + 1, j]   # c19 * A90
                        r = img[i - 1, j]   # c19 * A90
                    # angle 135
                    elif 112.5 <= angle[i, j] < 157.5:  # c20 * (((M - 2) * (N - 2)) - A0 - A45 - A90)
                        q = img[i - 1, j - 1]   # c19 * A135
                        r = img[i + 1, j + 1]   # c19 * A135

                    if (img[i, j] >= q) and (img[i, j] >= r):   # c21 * ((M - 2) * (N - 2))
                        Z[i, j] = img[i, j]     # c22 * Y
                    else:
                        Z[i, j] = 0     # c23 * (((M - 2) * (N - 2)) - Y)

                except IndexError as e:     # c24 * 0
                    pass    # c25 * 0

    return Z

def double_threshold(img, lowRatio=0.05, highRatio=0.09):
    highThreshold = img.max() * highRatio   # c26 * 1
    lowThreshold = highThreshold * lowRatio     # c27 * 1

    M, N = img.shape     # c10 * 1
    res = np.zeros((M, N))  # c11 * 1

    strong = 255  # c17 * 1
    weak = 25     # c17 * 1
    zero = 0      # c17 * 1

    strong_i, strong_j = np.where(img >= highThreshold)     # c28 * 1
    zeros_i, zeros_j = np.where(img < lowThreshold)     # c28 * 1
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))   # c29 * 1

    res[strong_i, strong_j] = strong    # c30 * 1
    res[weak_i, weak_j] = weak      # c30 * 1
    res[zeros_i, zeros_j] = zero    # c30 * 1

    return res, weak

def hysteresis(img, weak, strong=255):
    M, N = img.shape    # c10 * 1
    for i in range(1, M - 1):   # c14 * (M - 2)
        for j in range(1, N - 1):   # c15 * ((M - 2) * (N - 2))
            if img[i, j] == weak:   # c31 * ((M - 2) * (N - 2))
                try:    # c16 * (((M - 2) * (N - 2)) - Z)
                    if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                            or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                            or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                    img[i - 1, j + 1] == strong)):  # c32 * (((M - 2) * (N - 2)) - Z)
                        img[i, j] = strong  # c33 * (((M - 2) * (N - 2)) - Z - S)
                    else:
                        img[i, j] = 0   # c23 * (((M - 2) * (N - 2)) - Z - T)
                except IndexError as e:     # c24 * 0
                    pass    # c25 * 0

    return img

def run():
    Tk().withdraw()
    showinfo('Picture',
             'Select you Image, you can Add Images you want to the Directory /Projektarbeit/Beispielbilder')
    imag = askopenfilename(initialdir="/Beispielbilder")
    img = cv2.imread(imag, 0)
    rgbim = cv2.imread(imag)
    start = time.time()
    blur = gaussian_blur(img)
    sobel = sobel_filter(blur)
    Z = non_max_suppression(sobel[0], sobel[1])
    res = double_threshold(Z)
    final = hysteresis(res[0], res[1])
    end = time.time()
    Time = format(end - start, '.5g')

    rgbim[final > 0] = [255,0,0]

    plt.subplot(331), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(332), plt.imshow(blur, cmap='gray')
    plt.title('Blur effect'), plt.xticks([]), plt.yticks([])
    plt.subplot(333), plt.imshow(sobel[0], cmap='gray')
    plt.title('Sobel Filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(334), plt.imshow(Z, cmap='gray')
    plt.title('NMS Algorithm'), plt.xticks([]), plt.yticks([])
    plt.subplot(335), plt.imshow(res[0], cmap='gray')
    plt.title('Threshold Effect'), plt.xticks([]), plt.yticks([])
    plt.subplot(336), plt.imshow(final, cmap='gray')
    plt.title('Final image'), plt.xticks([]), plt.yticks([])
    plt.subplot(337), plt.imshow(rgbim, cmap='gray')
    plt.title('Rot?'), plt.xticks([]), plt.yticks([])
    plt.figtext(0.5, 0.3, 'Benötigte Zeit: ' + Time + ' Sekunden', fontsize=8, va="top", ha="left")
    plt.show()

    return rgbim
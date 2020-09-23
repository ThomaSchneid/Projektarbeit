import cv2
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt


def get_small_image_matrix_from_picture():
    org_imag = cv2.imread("../Bilder/rauschen.png", 0)
    timag = np.delete(org_imag, range(org_imag.shape[0], 30, -1), 0)
    tsmall_imag = np.delete(timag, range(timag.shape[1], 15, -1), 1)

    small_imag = post_rectangle_with_edges_in_picture(tsmall_imag)

    return org_imag, small_imag

def post_rectangle_with_edges_in_picture(small_imag):
    for i in range(0, small_imag.shape[0]):
        for j in range(0, small_imag.shape[1]):
            small_imag[i][j] += 123
            if small_imag[i][j] >= 255:
                small_imag[i][j] = 255

    small_imag[3:5, 2:13] = small_imag[27:29, 2:13] = 23
    small_imag[3:27, 2:4] = small_imag[3:27, 13:15] = 23

    return small_imag

def rad_imag():
    showinfo('Picture',
             'Select you Image, you can Add Images you want to the Directory /Projektarbeit/Beispielbilder')
    imag = askopenfilename(initialdir="/Beispielbilder")
    img = cv2.imread(imag, 0)

    return img

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

def edge_finder():
    return 0

def starter():
    images = get_small_image_matrix_from_picture()
    small_imag = images[1]
    b = post_rectangle_with_edges_in_picture(small_imag)
    blur = gaussian_blur(b)
    sobel = sobel_filter(blur)
    plt.subplot(231), plt.imshow(b, cmap='gray')
    plt.title('small_image'), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(blur, cmap='gray')
    plt.title('Blur'), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(sobel[0], cmap='gray')
    plt.title('Sobel_G'), plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(sobel[1], cmap='gray')
    plt.title('Sobel_Theta'), plt.xticks([]), plt.yticks([])
    plt.show()

    return images[0], images[1], b
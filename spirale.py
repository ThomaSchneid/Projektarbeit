import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

def load_image():
    image = cv2.imread("Bilder/rauschen.png", 0)
    return image

def create_whitescreen(image):
    for i in range(image.shape[0]):
        image[i] = 255
    return image

def spiral(img, diff):
    x_length = img.shape[1]
    y_length = img.shape[0]

    px = 0

    while (y_length - (2 * px)) >= diff and (x_length - (2 * px)) >= diff:
        px += diff
        # links nach rechts oben
        img[px, px:x_length - (1 + px)] = 0
        # oben nach unten hinten
        img[px:y_length - (1 + px), x_length - (1 + px)] = 0
        # links nach rechts unten
        img[y_length - (1 + px), px:x_length - (1 + px)] = 0
        # oben nach unten vorne
        img[px:y_length - (1 + px), px] = 0
    return img



from Python.check_neighbours import *
import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import time

def load_image():
    image = cv2.imread("Bilder/rauschen.png", 0)
    return image

def create_whitescreen(image):
    for i in range(image.shape[0]):
        image[i] = 255
    return image

def spiral(img, diff):
    start = time.time()
    x_length = img.shape[1]
    y_length = img.shape[0]
    px = 1
    check_diff = diff
    if diff > 3:
        check_diff = 3

    while (y_length - 2 * px) >= diff and (x_length - 2 * px) >= diff:
        px += diff
        # links nach rechts oben
        for j in range(px, x_length - px):
            # img[px, j] = 0
            check_pixel((px, j), img, check_diff)
        # oben nach unten hinten
        for i in range(px, y_length - px):
            # img[i, x_length - px] = 0
            check_pixel((i, x_length - px), img, check_diff)
        # links nach rechts unten
        for j in range(px, x_length - px):
            # img[y_length - px, j] = 0
            check_pixel((y_length - px, j), img, check_diff)
        # oben nach unten vorne
        for i in range(px, y_length - px):
            # img[i, px] = 0
            check_pixel((i, px), img, check_diff)
    end = time.time()
    print(end - start)
    return img

def check_pixel(pos, image, diff):
    falling_diagonal = round(top_left(pos, image, diff) / bottom_right(pos, image, diff), 4)
    top_bottom = round(top(pos, image, diff) / bottom(pos, image, diff), 4)
    raising_diagonal = round(top_right(pos, image, diff) / bottom_left(pos, image, diff), 4)
    right_left = round(right(pos, image, diff) / left(pos, image, diff), 4)

    return top_bottom, raising_diagonal, right_left, falling_diagonal


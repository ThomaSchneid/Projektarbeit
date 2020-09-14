from Python.check_neighbours import *
import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import time

def load_image():
    image = cv2.imread("Bilder/Camera_obscura.jpg", 0)
    return image

def create_whitescreen(image):
    whitescreen = np.full((image.shape), 255)
    return whitescreen

def spiral(img, diff):
    start = time.time()
    whitescreen = create_whitescreen(img)
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
            whitescreen[px, j] = check_pixel((px, j), img, check_diff)
        # oben nach unten hinten
        for i in range(px, y_length - px):
            whitescreen[i, x_length - px] = check_pixel((i, x_length - px), img, check_diff)
        # links nach rechts unten
        for j in range(px, x_length - px):
            whitescreen[y_length - px, j] = check_pixel((y_length - px, j), img, check_diff)
        # oben nach unten vorne
        for i in range(px, y_length - px):
            whitescreen[i, px] = check_pixel((i, px), img, check_diff)
    end = time.time()
    print(end - start)
    return whitescreen

def check_pixel(pos, image, diff):
    check_array = []

    check_array.append(round(top_left(pos, image, diff) / bottom_right(pos, image, diff), 4))
    check_array.append(round(top(pos, image, diff) / bottom(pos, image, diff), 4))
    check_array.append(round(top_right(pos, image, diff) / bottom_left(pos, image, diff), 4))
    check_array.append(round(right(pos, image, diff) / left(pos, image, diff), 4))

    for idx, val in enumerate(check_array):
        if val > 1:
            check_array[idx] = round(1/val, 4)

    maxim = max(check_array)
    if maxim > 0.4:
        direction = check_array.index(maxim)
    else:
        direction = 255
    return direction

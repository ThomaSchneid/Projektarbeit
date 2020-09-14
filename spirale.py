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
    possible_directions = [0,1,2,3]
    check_diff = diff
    if diff > 3:
        check_diff = 3

    while (y_length - 2 * px) >= diff and (x_length - 2 * px) >= diff:
        px += diff
        # links nach rechts oben
        for j in range(px, x_length - px):
            direction = check_pixel((px, j), img, check_diff)
            whitescreen[px, j] = check_pixel((px, j), img, check_diff)
        # oben nach unten hinten
        for i in range(px, y_length - px):
            direction = check_pixel((i, x_length - px), img, check_diff)
            whitescreen[i, x_length - px] = check_pixel((i, x_length - px), img, check_diff)
        # links nach rechts unten
        for j in range(px, x_length - px):
            direction = check_pixel((y_length - px, j), img, check_diff)
            whitescreen[y_length - px, j] = check_pixel((y_length - px, j), img, check_diff)
        # oben nach unten vorne
        for i in range(px, y_length - px):
            direction = check_pixel((i, px), img, check_diff)
            whitescreen[i, px] = check_pixel((i, px), img, check_diff)
            if direction in possible_directions:
                check_next_pixel_up_down(whitescreen, img, i, px, check_diff, direction)
    end = time.time()
    print(end - start)
    return whitescreen

def check_pixel(pos, image, diff):
    check_array = []

    check_array.append(top_left(pos, image, diff) - bottom_right(pos, image, diff))
    check_array.append(top(pos, image, diff) - bottom(pos, image, diff))
    check_array.append(top_right(pos, image, diff) - bottom_left(pos, image, diff))
    check_array.append(right(pos, image, diff) - left(pos, image, diff))

    maxim = max(check_array, key = abs)
    if abs(maxim) > 20:
        direction = check_array.index(maxim)
        # Wenn es keine Kante ist wird dem Pixel der Wert 255 zugeordnet
    else:
        direction = 255
    return direction


def check_next_pixelup_down(whitescreen, img, i, px, check_diff, direction):
    if direction == 0:
        check_pixel((i + 1, px - 1))
    return true
from Python.check_neighbours import *
from helper import *
from scipy import ndimage
import matplotlib.pyplot as plt
import time

def spiral(img, diff):
    start = time.time()
    whitescreen = create_whitescreen(img)
    x_length = img.shape[1]
    y_length = img.shape[0]
    # y_length, x_length = img.shape
    px = 0
    possible_dirs = [0, 1, 2, 3]
    check_diff = diff
    if diff > 3:
        check_diff = 3

    while (y_length - 2 * px) >= diff and (x_length - 2 * px) >= diff:
        px += diff
        # links nach rechts oben
        for j in range(px, x_length - px):
            dir = check_pixel((px, j), img, check_diff)
            whitescreen[px, j] = dir
            if dir in possible_dirs:
                check_first_pixel_left_right_top(whitescreen, img, px, j, check_diff, dir)
        # oben nach unten hinten
        for i in range(px, y_length - px):
            dir = check_pixel((i, x_length - px), img, check_diff)
            whitescreen[i, x_length - px] = dir
            if dir in possible_dirs:
                check_first_pixel_up_down_back(whitescreen, img, i, x_length - px, check_diff, dir)
        # links nach rechts unten
        for j in range(px, x_length - px):
            direction = check_pixel((y_length - px, j), img, check_diff)
            whitescreen[y_length - px, j] = direction
            if dir in possible_dirs:
                check_first_pixel_left_right_bottom(whitescreen, img, y_length - px, j, check_diff, dir)
        # oben nach unten vorne
        for i in range(px, y_length - px):
            dir  = check_pixel((i, px), img, check_diff)
            whitescreen[i, px] = dir
            if dir in possible_dirs:
                check_first_pixel_up_down_front(whitescreen, img, i, px, check_diff, dir)
    end = time.time()
    print(end - start)
    return whitescreen





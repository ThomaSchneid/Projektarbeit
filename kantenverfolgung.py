from Python.check_neighbours import *
from helper import *
import cv2
import numpy as np
import matplotlib as plt
import time

def edge_tracker(img, diff):
    start = time.time()
    whitescreen = create_whitescreen(img)
    x_length = img.shape[1]
    y_length = img.shape[0]
    px = diff

    while diff <= y_length:
        for j in range(px, x_length - px):
            whitescreen[diff, j] = 0

        diff += px
    end = time.time()
    print(end - start)
    return whitescreen

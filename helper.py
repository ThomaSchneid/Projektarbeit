import cv2
import numpy as np


def load_image():
    image = cv2.imread("Bilder/Camera_obscura.jpg", 0)
    return image

def create_whitescreen(image):
    whitescreen = np.full((image.shape), 255)
    return whitescreen
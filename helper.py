from imports import *

def load_image():
    image = cv2.imread("Bilder/Camera_obscura.jpg", 0)
    return image

def create_whitescreen(image):
    whitescreen = np.full((image.shape), 254)
    return whitescreen
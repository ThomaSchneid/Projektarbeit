import cv2
import numpy as np
from scipy import ndimage

# NOISE REDUCTION
# Gaussian 5 x 5 Kernel

def gaussian_kernel(size, sigma=1.8):
    size = int(size) // 2
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    normal = 1 / (2.0 * np.pi * sigma ** 2)
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal
    return g


def gaussian_blur():
    img = cv2.imread("Bilder/hochschule.png", 0)
    blur = cv2.GaussianBlur(img, (5, 5), 1.4)
    cv2.imshow("Show blur effect", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return blur

# GRADIENT CALCULATION
# Sobel Filter

def sobel_filter(img):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    Ix = ndimage.filters.convolve(img, Gx).astype(float)
    Iy = ndimage.filters.convolve(img, Gy).astype(float)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan(Iy, Ix)

    cv2.imshow("Image after sobel", G)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return G, theta


# NON MAXIMUM SUPPRESSION
# Create a matrix initialized to 0 of the same size of the original gradient intesity matrix
# Identify the edge direction based on the angle  value from the angle matrix
# Check if the pixel in the same direction has a higher intensity than the pixel that is currently processed
# Return the image processed with the non-max suppression algorithm

def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M, N))
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            try:
                q = 255
                r = 255

                # angle 0
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = img[i, j + 1]
                    r = img[i, j - 1]
                # angle 45
                elif 22.5 <= angle[i, j] < 67.5:
                    q = img[i + 1, j - 1]
                    r = img[i - 1, j + 1]
                # angle 90
                elif 67.5 <= angle[i, j] < 112.5:
                    q = img[i + 1, j]
                    r = img[i - 1, j]
                # angle 135
                elif 112.5 <= angle[i, j] < 157.5:
                    q = img[i - 1, j - 1]
                    r = img[i + 1, j + 1]

                if (img[i, j] >= q) and (img[i, j] >= r):
                    Z[i, j] = img[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    cv2.imshow("Image after non-max-suppression", Z)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return Z


# DOUBLE THRESHOLD

def double_threshold(img, lowRatio=0.05, highRatio=0.09):
    highThreshold = img.max() * highRatio
    lowThreshold = highThreshold * lowRatio

    M, N = img.shape
    res = np.zeros((M, N))

    strong = np.int32(255)
    weak = np.int32(25)
    zero = np.int32(0)

    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    res[zeros_i, zeros_j] = zero

    cv2.imshow("Image after double threshold", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return res, weak, strong


# EDGE TRACKING BY HYSTERESIS
# Transform weak pixels in strong pixels


def hysteresis(img, weak, strong=255):
    M, N = img.shape
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if img[i, j] == weak:
                try:
                    if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                            or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                            or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                    img[i - 1, j + 1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass

    cv2.imshow("Final image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def test():
    blur = gaussian_blur()
    sobel = sobel_filter(blur)
    Z = non_max_suppression(sobel[0], sobel[1])
    res = double_threshold(Z)
    final = hysteresis(res[0], res[1])
    return final
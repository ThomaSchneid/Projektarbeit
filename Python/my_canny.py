from Python.helper import *

def g_kern(mask, sigm=1.8):
    mask = int(mask) // 2   # c1 * 1
    x, y = np.mgrid[-mask:mask + 1, -mask:mask + 1]     # c2 * 1
    norm = 1 / (2 * np.pi * sigm ** 2)     # c3 * 1
    kern = np.exp(-((x ** 2 + y ** 2) / (2 * sigm ** 2))) * norm      # c4 * 1

    return kern

def gaussian_blur(img):
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    return blur

def sobel(img):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)     #c5 * 1
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)     #c5 * 1

    ablx = ndimage.filters.convolve(img, Gx).astype(float)    # c6 * 1
    ably = ndimage.filters.convolve(img, Gy).astype(float)    # c6 * 1

    res = np.hypot(ablx, ably)    # c7 * 1
    res = res / res.max() * 255   # c8 * 1
    gradient = np.arctan(ably, ablx)   # c9 * 1

    return res, gradient

def non_max_suppression(img, grad):
    y, x = img.shape    # c10 * 1
    blackscreen = np.zeros(img.shape)    # c11 * 1
    angle = grad * 180. / np.pi    # c12 * 1
    angle[angle < 0] += 180     # c13 * 1

    for i in range(1, y - 1):   # c14 * M - 2
        for j in range(1, x - 1):   # c15 * ((M - 2) * (N - 2))
            if img[i, j] != 0:
                try:    # c16 * ((M - 2) * (N - 2))
                    q = 255     # c17 * ((M - 2) * (N - 2))
                    r = 255     # c17 * ((M - 2) * (N - 2))

                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):  # c18 * ((M - 2) * (N - 2))
                        q = img[i, j + 1]   # c19 * A0
                        r = img[i, j - 1]   # c19 * A0
                    # angle 45
                    elif 22.5 <= angle[i, j] < 67.5:    # c20 * (((M - 2) * (N - 2)) - A0)
                        q = img[i + 1, j - 1]   # c19 * A45
                        r = img[i - 1, j + 1]   # c19 * A45
                    # angle 90
                    elif 67.5 <= angle[i, j] < 112.5:   # c20 * (((M - 2) * (N - 2)) - A0 - A45)
                        q = img[i + 1, j]   # c19 * A90
                        r = img[i - 1, j]   # c19 * A90
                    # angle 135
                    elif 112.5 <= angle[i, j] < 157.5:  # c20 * (((M - 2) * (N - 2)) - A0 - A45 - A90)
                        q = img[i - 1, j - 1]   # c19 * A135
                        r = img[i + 1, j + 1]   # c19 * A135

                    if (img[i, j] >= q) and (img[i, j] >= r):   # c21 * ((M - 2) * (N - 2))
                        blackscreen[i, j] = img[i, j]     # c22 * Y
                    else:
                        blackscreen[i, j] = 0     # c23 * (((M - 2) * (N - 2)) - Y)

                except IndexError as e:     # c24 * 0
                    pass    # c25 * 0

    return blackscreen

def double_threshold(img, unterer_faktor=0.05, oberer_faktor=0.09):
    obere_schwelle = img.max() * oberer_faktor   # c26 * 1
    untere_schwelle = obere_schwelle * unterer_faktor     # c27 * 1

    blackscreen = np.zeros(img.shape)  # c11 * 1

    starkes_pixel = 255  # c17 * 1
    schwaches_pixel = 25     # c17 * 1
    keine_kante = 0      # c17 * 1

    starkes_pixel_i, starkes_pixel_j = np.where(img >= obere_schwelle)     # c28 * 1
    keine_kante_i, keine_kante_j = np.where(img <= untere_schwelle)     # c28 * 1
    schwaches_pixel_i, schwaches_pixel_j = np.where((img < obere_schwelle) & (img > untere_schwelle))   # c29 * 1

    blackscreen[starkes_pixel_i, starkes_pixel_j] = starkes_pixel    # c30 * 1
    blackscreen[schwaches_pixel_i, schwaches_pixel_j] = schwaches_pixel      # c30 * 1
    blackscreen[keine_kante_i, keine_kante_j] = keine_kante    # c30 * 1

    return blackscreen

def hysterese(img, schwaches_pixel, starkes_pixel=255):
    y, x = img.shape    # c10 * 1
    for i in range(1, y - 1):   # c14 * (M - 2)
        for j in range(1, x - 1):   # c15 * ((M - 2) * (N - 2))
            if img[i, j] == schwaches_pixel:   # c31 * ((M - 2) * (N - 2))
                try:    # c16 * (((M - 2) * (N - 2)) - Z)
                    if ((img[i + 1, j - 1] == starkes_pixel) or (img[i + 1, j] == starkes_pixel) or (img[i + 1, j + 1] == starkes_pixel)
                            or (img[i, j - 1] == starkes_pixel) or (img[i, j + 1] == starkes_pixel)
                            or (img[i - 1, j - 1] == starkes_pixel) or (img[i - 1, j] == starkes_pixel) or (
                                    img[i - 1, j + 1] == starkes_pixel)):  # c32 * (((M - 2) * (N - 2)) - Z)
                        img[i, j] = starkes_pixel  # c33 * (((M - 2) * (N - 2)) - Z - S)
                    else:
                        img[i, j] = 0   # c23 * (((M - 2) * (N - 2)) - Z - T)
                except IndexError as e:     # c24 * 0
                    pass    # c25 * 0

    return img

def test_canny():
    image = load_image()
    start = time.time()
    res = cv2.Canny(image, 100, 200)
    end = time.time()
    print(end - start)

    return res

def run():
    image = load_image()
    start = time.time()
    sob = sobel(image)
    nms = non_max_suppression(sob[0], sob[1])
    dt = double_threshold(nms)
    res = hysterese(dt, 25)
    end = time.time()
    print(end - start)
    return res
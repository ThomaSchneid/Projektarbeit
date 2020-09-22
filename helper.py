from imports import *

def load_image():
    image = cv2.imread("Bilder/Camera_obscura.jpg", 0)
    return image

def create_whitescreen(image):
    whitescreen = np.full((image.shape), 254)
    return whitescreen

def subplots(rows, columns, images):
    add = 1
    position = rows * 100 + columns * 10 + add
    for img in images:
        plt.subplot(position), plt.imshow(img, cmap='gray')
        plt.title('Bild 1'), plt.xticks([]), plt.yticks([])
        add += 1

    plt.show()

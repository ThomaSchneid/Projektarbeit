from imports import *

def load_image():
    image = cv2.imread("Bilder/stoerung.jpg", 0)
    return image

def create_whitescreen(image):
    whitescreen = np.full((image.shape), 254)
    return whitescreen

def subplots(images):
    add = 1
    amount = len(images)
    rows = int(amount / 3) * 100
    if rows == 0:
        rows = 100
    columns = (amount % 3) * 10
    if columns == 0:
        columns = 10
    for img in images:
        position = columns + rows + add
        plt.subplot(position), plt.imshow(img, cmap='gray')
        plt.title('Bild' + str(add)), plt.xticks([]), plt.yticks([])
        add += 1

    plt.show()

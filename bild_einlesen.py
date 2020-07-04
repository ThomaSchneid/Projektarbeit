import cv2
import numpy as np
import xlwt
from xlwt import Workbook
import time

def japan():
    japan = cv2.imread("japan.png", 0)
    return japan

def rauschen():
    rauschen = cv2.imread("rauschen.png", 0)
    return rauschen

def test_canny(img):
    start = time.time()

    cv2.imshow("An example image", img)
    cv2.imshow("Canny picture", cv2.Canny(img, 50, 200))
    end = time.time()
    print(end - start)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def fill_workbook(img):
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    for x in range(0,255):
        for y in range(0,255):
            sheet1.write(x, y, int(img[y][x]))


    wb.save('xlwt example.xls')

def schwelle(img):
    start = time.time()
    test = img
    faktor = 20
    mean = img.mean()
    schwelle_unten = mean - (mean / 100) * faktor

    img[img < schwelle_unten] = 0

    cv2.imshow("Original image", img)
    cv2.imshow("Original image", test)
    cv2.imshow("Canny picture", cv2.Canny(img, schwelle_unten, 255))
    end = time.time()
    print(end - start)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def add_dim(img):
    add_matrix = np.zeros((1,img.shape[0], img.shape[1]))
    expand_img = np.expand_dims(img, axis = 0)
    result = np.concatenate((expand_img, add_matrix), axis = 0)
    return result

def run(img):
    print(add_dim(img))
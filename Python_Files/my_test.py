import cv2
import numpy as np
import time
from scipy import ndimage
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import matplotlib.pyplot as plt
from my_canny import *

Tk().withdraw()
showinfo('Picture',
         'Select you Image, you can Add Images you want to the Directory /Projektarbeit/Beispielbilder')
imag = askopenfilename(initialdir="/Beispielbilder")
img = cv2.imread(imag, 0)
rgbim = cv2.imread(imag)
start = time.time()
blur = gaussian_blur(img)
sobel = sobel_filter(blur)
Z = non_max_suppression(sobel[0], sobel[1])
res = double_threshold(Z)
final = hysteresis(res[0], res[1])
end = time.time()
Time = format(end - start, '.5g')

rgbim[final > 0] = [255,0,0]

plt.subplot(331), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(332), plt.imshow(blur, cmap='gray')
plt.title('Blur effect'), plt.xticks([]), plt.yticks([])
plt.subplot(333), plt.imshow(sobel[0], cmap='gray')
plt.title('Sobel Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(334), plt.imshow(Z, cmap='gray')
plt.title('NMS Algorithm'), plt.xticks([]), plt.yticks([])
plt.subplot(335), plt.imshow(res[0], cmap='gray')
plt.title('Threshold Effect'), plt.xticks([]), plt.yticks([])
plt.subplot(336), plt.imshow(final, cmap='gray')
plt.title('Final image'), plt.xticks([]), plt.yticks([])
plt.subplot(337), plt.imshow(rgbim, cmap='gray')
plt.title('Rot?'), plt.xticks([]), plt.yticks([])
plt.figtext(0.5, 0.3, 'Benötigte Zeit: ' + Time + ' Sekunden', fontsize=8, va="top", ha="left")
plt.show()
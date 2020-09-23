from Python.helper import *

Tk().withdraw()
showinfo('Picture',
         'Select you Image, you can Add Images you want to the Directory /Projektarbeit/Beispielbilder')
imag = askopenfilename(initialdir="Beispielbilder")
img = cv2.imread(imag, 0)
start = time.time()
final = cv2.Canny(img, 100, 200)
end = time.time()
Time = format(end - start, '.5g')

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(final, cmap='gray')
plt.title('Canny Algorithm'), plt.xticks([]), plt.yticks([])
plt.figtext(0.4, 0.05, 'Benötigte Zeit: ' + Time + ' Sekunden', fontsize=8, va="top", ha="left")
plt.show()
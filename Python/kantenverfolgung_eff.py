from Python.helper import *
from Python.check_neighbours_efficient import *

def edge_tracker(diff):
    # img = load_image()
    start = time.time()
    whitescreen = create_whitescreen(img)
    x_length = img.shape[1]
    y_length = img.shape[0]
    px = 0
    check_diff = diff

    if diff > 3:
        check_diff = 3

    while px <= y_length - 2 * diff - 1:
        px += diff
        for j in range(check_diff, x_length - check_diff):
            next_pixel_pos = (px, j)
            if whitescreen[next_pixel_pos] == 254:
                dir = check_pixel((px, j), img)
                whitescreen[next_pixel_pos] = dir

                npparr = []
                dirarr = []

                while (dir != 255) and (check_diff < next_pixel_pos[0] < (y_length - check_diff - 1)) and (check_diff + 1 < next_pixel_pos[1] < (x_length - check_diff - 1)):
                    next_pixel_pos = set_next_pixel_position(next_pixel_pos, dir)
                    dir = check_pixel(next_pixel_pos, img)
                    npparr.append(next_pixel_pos)
                    dirarr.append(dir)

                if len(npparr) > 3:
                    for pos in npparr:
                        whitescreen[pos] = dirarr[npparr.index(pos)]
                else:
                    for pos in npparr:
                        whitescreen[pos] = 255

    end = time.time()
    print(end - start)
    return whitescreen

def set_next_pixel_position(next_pixel_pos, dir):
    _px = next_pixel_pos[0]
    _j = next_pixel_pos[1]
    if dir == 0:
        next_pixel_pos = (_px + 1, _j - 1)
    elif dir == 1:
        next_pixel_pos = (_px, _j + 1)
    elif dir == 2:
        next_pixel_pos = (_px + 1, _j + 1)
    elif dir == 3:
        next_pixel_pos = (_px + 1, _j)
    return next_pixel_pos

Tk().withdraw()
showinfo('Picture',
         'Select you Image, you can Add Images you want to the Directory /Projektarbeit/Beispielbilder')
imag = askopenfilename(initialdir="Beispielbilder")
img = cv2.imread(imag, 0)
start = time.time()
final = edge_tracker(3)
end = time.time()
Time = format(end - start, '.5g')

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(final, cmap='gray')
plt.title('Edge tracking algorithm'), plt.xticks([]), plt.yticks([])
plt.figtext(0.4, 0.05, 'Benötigte Zeit: ' + Time + ' Sekunden', fontsize=8, va="top", ha="left")
plt.show()
##########################
###  CHECK MAIN PIXEL  ###
##########################

def top(pos, img):
    sum_top = 0
    for j in range(1, 3):
        sum_top += img[pos[0], pos[1] + j]

    return sum_top/2

def bottom(pos, img):
    sum_bottom = 0
    for j in range(1, 3):
        sum_bottom += img[pos[0], pos[1] - j]

    return sum_bottom/2

def left(pos, img):
    sum_left = 0
    for i in range(1, 3):
        sum_left += img[pos[0] - i, pos[1]]

    return sum_left/2

def right(pos, img):
    sum_right = 0
    for i in range(1, 3):
        sum_right += img[pos[0] + i, pos[1]]

    return sum_right/2

def top_left(pos, img):
    sum_top_left = 0
    for i in range(1, 3):
        sum_top_left += img[pos[0] - i, pos[1] - i]

    return sum_top_left/2


def top_right(pos, img):
    sum_top_right = 0
    for i in range(1, 3):
        sum_top_right += img[pos[0] - i, pos[1] + i]

    return sum_top_right/2

def bottom_left(pos, img):
    sum_bot_left = 0
    for i in range(1, 3):
        sum_bot_left += img[pos[0] + i, pos[1] - i]

    return sum_bot_left/2

def bottom_right(pos, img):
    sum_bot_right = 0
    for i in range(1, 3):
        sum_bot_right += img[pos[0] + i, pos[1] + i]

    return sum_bot_right/2

##########################
## CHECK CURRENT PIXEL ##
##########################

def check_pixel(pos, image):
    check_array = []

    check_array.append(top_left(pos, image) - bottom_right(pos, image))
    check_array.append(top(pos, image) - bottom(pos, image))
    check_array.append(top_right(pos, image) - bottom_left(pos, image))
    check_array.append(right(pos, image) - left(pos, image))

    maxim = max(check_array, key = abs)
    if abs(maxim) > 20:
        direction = check_array.index(maxim)
        # Wenn es keine Kante ist wird dem Pixel der Wert 255 zugewiesen
    else:
        direction = 255
    return direction

##########################
# CHECK NEIGHBOUR PIXEL  #
##########################

def check_first_pixel_up_down_front(whitescreen, img, i, px, dir):
    if dir == 0:
        pixel = check_pixel((i - 1, px + 1), img)
        whitescreen[i - 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i - 1, px + 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 1:
        pixel = check_pixel((i, px + 1), img)
        whitescreen[i, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i, px + 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i + 1, px + 1), img)
        whitescreen[i + 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i + 1, px + 1, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_up_down_front(whitescreen, img, i, px, dir):
    if dir == 0:
        whitescreen[i - 1, px + 1] = check_pixel((i - 1, px + 1), img)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img)
    elif dir == 2:
        whitescreen[i + 1, px + 1] = check_pixel((i + 1, px + 1), img)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img)
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img)
    return

def check_first_pixel_left_right_bottom(whitescreen, img, i, px, dir):
    if dir == 0:
        pixel = check_pixel((i - 1, px + 1), img)
        whitescreen[i - 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px + 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i - 1, px - 1), img)
        whitescreen[i - 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px - 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 3:
        pixel = check_pixel((i - 1, px), img)
        whitescreen[i - 1, px] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px, pixel)
    return

def check_second_pixel_left_right_bottom(whitescreen, img, i, px, dir):
    if dir == 0:
        whitescreen[i - 1, px + 1] = check_pixel((i - 1, px + 1), img)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img)
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img)
    elif dir == 2:
        whitescreen[i - 1, px - 1] = check_pixel((i - 1, px - 1), img)
    elif dir == 3:
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img)
    return

def check_first_pixel_up_down_back(whitescreen, img, i, px, dir):
    if dir == 0:
        pixel = check_pixel((i + 1, px - 1), img)
        whitescreen[i + 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i + 1, px - 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 1:
        pixel = check_pixel((i, px - 1), img)
        whitescreen[i, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i, px - 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i - 1, px - 1), img)
        whitescreen[i - 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i - 1, px - 1, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_up_down_back(whitescreen, img, i, px, dir):
    if dir == 0:
        whitescreen[i + 1, px - 1] = check_pixel((i + 1, px - 1), img)
    elif dir == 1:
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img)
    elif dir == 2:
        whitescreen[i - 1, px - 1] = check_pixel((i - 1, px - 1), img)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img)
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img)
    return

def check_first_pixel_left_right_top(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        pixel = check_pixel((i + 1, px - 1), img)
        whitescreen[i + 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px - 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i + 1, px + 1), img)
        whitescreen[i + 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px + 1, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 3:
        pixel = check_pixel((i + 1, px), img)
        whitescreen[i + 1, px] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_left_right_top(whitescreen, img, i, px, dir):
    if dir == 0:
        whitescreen[i + 1, px - 1] = check_pixel((i + 1, px - 1), img)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img)
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img)
    elif dir == 2:
        whitescreen[i + 1, px + 1] = check_pixel((i + 1, px + 1), img)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img)
    return

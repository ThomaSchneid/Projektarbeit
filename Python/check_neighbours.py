##########################
###  CHECK MAIN PIXEL  ###
##########################

def top(pos, img, diff):
    list = [-1,0,1]
    sum_top = 0
    for i in range(1, diff + 1):
        for j in list:
            sum_top += img[pos[0] - i][pos[1] + j]

    return sum_top/(3 * diff)

def bottom(pos, img, diff):
    list = [-1, 0, 1]
    sum_bottom = 0
    for i in range(1, diff + 1):
        for j in list:
            sum_bottom += img[pos[0] + i][pos[1] + j]

    return sum_bottom/(3 * diff)

def left(pos, img, diff):
    list = [-1, 0, 1]
    sum_left = 0
    for j in range(1, diff + 1):
        for i in list:
            sum_left += img[pos[0] + i][pos[1] - j]

    return sum_left/(3 * diff)

def right(pos, img, diff):
    list = [-1, 0, 1]
    sum_right = 0
    for j in range(1, diff + 1):
        for i in list:
            sum_right += img[pos[0] + i][pos[1] + j]

    return sum_right/(3 * diff)

def top_left(pos, img, diff):
    sum_top_left = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_top_left += img[pos[0] - i][pos[1] - j]

    sum_top_left -= img[pos]

    return sum_top_left/((3 * diff + 1) - 1)


def top_right(pos, img, diff):
    sum_top_right = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_top_right += img[pos[0] - i][pos[1] + j]

    sum_top_right -= img[pos]

    return sum_top_right/((3 * diff + 1) - 1)

def bottom_left(pos, img, diff):
    sum_bot_left = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_bot_left += img[pos[0] + i][pos[1] - j]

    sum_bot_left -= img[pos]
    return sum_bot_left/((3 * diff + 1) - 1)

def bottom_right(pos, img, diff):
    sum_bot_right = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_bot_right += img[pos[0] + i][pos[1] + j]

    sum_bot_right -= img[pos]
    return sum_bot_right/((3 * diff + 1) - 1)

##########################
## CHECK CURRENT PIXEL ##
##########################

def check_pixel(pos, image, diff):
    check_array = []

    check_array.append(top_left(pos, image, diff) - bottom_right(pos, image, diff))
    check_array.append(top(pos, image, diff) - bottom(pos, image, diff))
    check_array.append(top_right(pos, image, diff) - bottom_left(pos, image, diff))
    check_array.append(right(pos, image, diff) - left(pos, image, diff))

    maxim = max(check_array, key = abs)
    #todo Schwelle ersetzen
    if abs(maxim) > 20:
        direction = check_array.index(maxim)
        # Wenn es keine Kante ist wird dem Pixel der Wert 255 zugewiesen
    else:
        direction = 255
    return direction

##########################
# CHECK NEIGHBOUR PIXEL  #
##########################

def check_first_pixel_up_down_front(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        pixel = check_pixel((i - 1, px + 1), img, diff)
        whitescreen[i - 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i - 1, px + 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 1:
        pixel = check_pixel((i, px + 1), img, diff)
        whitescreen[i, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i, px + 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i + 1, px + 1), img, diff)
        whitescreen[i + 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_front(whitescreen, img, i + 1, px + 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_up_down_front(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        whitescreen[i - 1, px + 1] = check_pixel((i - 1, px + 1), img, diff)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img, diff)
    elif dir == 2:
        whitescreen[i + 1, px + 1] = check_pixel((i + 1, px + 1), img, diff)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img, diff)
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img, diff)
    return

def check_first_pixel_left_right_bottom(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        pixel = check_pixel((i - 1, px + 1), img, diff)
        whitescreen[i - 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px + 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i - 1, px - 1), img, diff)
        whitescreen[i - 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px - 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 3:
        pixel = check_pixel((i - 1, px), img, diff)
        whitescreen[i - 1, px] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i - 1, px, diff, pixel)
    return

def check_second_pixel_left_right_bottom(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        whitescreen[i - 1, px + 1] = check_pixel((i - 1, px + 1), img, diff)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img, diff)
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img, diff)
    elif dir == 2:
        whitescreen[i - 1, px - 1] = check_pixel((i - 1, px - 1), img, diff)
    elif dir == 3:
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img, diff)
    return

def check_first_pixel_up_down_back(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        pixel = check_pixel((i + 1, px - 1), img, diff)
        whitescreen[i + 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i + 1, px - 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 1:
        pixel = check_pixel((i, px - 1), img, diff)
        whitescreen[i, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i, px - 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i - 1, px - 1), img, diff)
        whitescreen[i - 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_up_down_back(whitescreen, img, i - 1, px - 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_up_down_back(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        whitescreen[i + 1, px - 1] = check_pixel((i + 1, px - 1), img, diff)
    elif dir == 1:
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img, diff)
    elif dir == 2:
        whitescreen[i - 1, px - 1] = check_pixel((i - 1, px - 1), img, diff)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img, diff)
        whitescreen[i - 1, px] = check_pixel((i - 1, px), img, diff)
    return

def check_first_pixel_left_right_top(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        pixel = check_pixel((i + 1, px - 1), img, diff)
        whitescreen[i + 1, px - 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px - 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 2:
        pixel = check_pixel((i + 1, px + 1), img, diff)
        whitescreen[i + 1, px + 1] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px + 1, diff, pixel)
        else:
            whitescreen[i, px] = 255
    elif dir == 3:
        pixel = check_pixel((i + 1, px), img, diff)
        whitescreen[i + 1, px] = pixel
        if pixel != 255:
            check_second_pixel_left_right_bottom(whitescreen, img, i + 1, px, diff, pixel)
        else:
            whitescreen[i, px] = 255
    return

def check_second_pixel_left_right_top(whitescreen, img, i, px, diff, dir):
    if dir == 0:
        whitescreen[i + 1, px - 1] = check_pixel((i + 1, px - 1), img, diff)
    elif dir == 1:
        whitescreen[i, px + 1] = check_pixel((i, px + 1), img, diff)
        whitescreen[i, px - 1] = check_pixel((i, px - 1), img, diff)
    elif dir == 2:
        whitescreen[i + 1, px + 1] = check_pixel((i + 1, px + 1), img, diff)
    elif dir == 3:
        whitescreen[i + 1, px] = check_pixel((i + 1, px), img, diff)
    return

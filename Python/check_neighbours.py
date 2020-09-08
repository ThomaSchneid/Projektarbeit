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
    sum_bottom_left = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_bottom_left += img[pos[0] + i][pos[1] - j]

    sum_bottom_left -= img[pos]

    return sum_bottom_left/((3 * diff + 1) - 1)

def bottom_right(pos, img, diff):
    sum_bottom_right = 0
    for j in range(0, diff + 1):
        for i in range(0, diff + 1):
            sum_bottom_right += img[pos[0] + i][pos[1] + j]

    sum_bottom_right -= img[pos]

    return sum_bottom_right/((3 * diff + 1) - 1)

def value_top_bottom(pos, img):
    if img[pos[0] - 1][pos[1]] > img[pos[0] + 1][pos[1]]:
        moving_direction = 2
    else:
        moving_direction = 7

    return moving_direction

def value_left_right(pos, img):
    if img[pos[0]][pos[1] - 1] > img[pos[0]][pos[1] + 1]:
        moving_direction = 4
    else:
        moving_direction = 5

    return moving_direction

def value_falling_diagonal(pos, img):
    if img[pos[0] - 1][pos[1] - 1] > img[pos[0] + 1][pos[1] + 1]:
        moving_direction = 1
    else:
        moving_direction = 8

    return moving_direction

def value_raising_diagonal(pos, img):
    if img[pos[0] - 1][pos[1] + 1] > img[pos[0] + 1][pos[1] - 1]:
        moving_direction = 3
    else:
        moving_direction = 6

    return moving_direction
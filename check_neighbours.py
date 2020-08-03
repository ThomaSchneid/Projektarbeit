def top(pos, img):
    list = [-1,0,1]
    sum_top = 0
    for a in list:
        sum_top += img[pos[0] - 1][pos[1] + a]

    return sum_top

def bottom(pos, img):
    list = [-1, 0, 1]
    sum_bottom = 0
    for a in list:
        sum_bottom += img[pos[0] + 1][pos[1] + a]

    return sum_bottom

def left(pos, img):
    list = [-1, 0, 1]
    sum_left = 0
    for a in list:
        sum_left += img[pos[0] + a][pos[1] - 1]

    return sum_left

def right(pos, img):
    list = [-1, 0, 1]
    sum_right = 0
    for a in list:
        sum_right += img[pos[0] + a][pos[1] + 1]

    return sum_right

def diagonal_top_left(pos, img):
    list = [-1, 0]
    sum_diagonal_top_left = 0
    for a in list:
        sum_diagonal_top_left += img[pos[0] + a][pos[1] - 1]

    sum_diagonal_top_left += img[pos[0] - 1][pos[1]]

    return sum_diagonal_top_left

def diagonal_top_right(pos, img):
    list = [-1, 0]
    sum_diagonal_top_right = 0
    for a in list:
        sum_diagonal_top_right += img[pos[0] + a][pos[1] + 1]

    sum_diagonal_top_right += img[pos[0] - 1][pos[1]]

    return sum_diagonal_top_right

def diagonal_bottom_left(pos, img):
    list = [0, 1]
    sum_diagonal_bottom_left = 0
    for a in list:
        sum_diagonal_bottom_left += img[pos[0] + a][pos[1] - 1]

    sum_diagonal_bottom_left += img[pos[0] + 1][pos[1]]

    return sum_diagonal_bottom_left

def diagonal_bottom_right(pos, img):
    list = [0, 1]
    sum_diagonal_bottom_right = 0
    for a in list:
        sum_diagonal_bottom_right += img[pos[0] + a][pos[1] + 1]

    sum_diagonal_bottom_right += img[pos[0] + 1][pos[1]]

    return sum_diagonal_bottom_right

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
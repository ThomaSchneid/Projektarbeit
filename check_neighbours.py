def top(pos, img):
    list = [-1,0,1]
    sum_top = 0
    average_top = 0
    for a in list:
        sum_top += img[pos[0] - 1][pos[1] + a]

    average_top = sum_top / 3
    return average_top

def bottom(pos, img):
    list = [-1, 0, 1]
    sum_bottom = 0
    average_bottom = 0
    for a in list:
        sum_bottom += img[pos[0] + 1][pos[1] + a]

    average_bottom = sum_bottom / 3
    return average_bottom

def left(pos, img):
    list = [-1, 0, 1]
    sum_left = 0
    average_left = 0
    for a in list:
        sum_left += img[pos[0] + a][pos[1] - 1]

    average_left = sum_left / 3
    return average_left

def right(pos, img):
    list = [-1, 0, 1]
    sum_right = 0
    average_right = 0
    for a in list:
        sum_right += img[pos[0] + a][pos[1] + 1]

    average_right = sum_right / 3
    return average_right

def diagonal_top_left(pos, img):
    list = [-1, 0]
    sum_diagonal = 0
    average_diagonal = 0
    for a in list:
        sum_diagonal += img[pos[0] + a][pos[1] - 1]

    sum_diagonal += img[pos[0] - 1][pos[1]]
    average_diagonal = sum_diagonal / 3
    return average_diagonal

def diagonal_top_right(pos, img):
    list = [-1, 0]
    sum_diagonal = 0
    average_diagonal = 0
    for a in list:
        sum_diagonal += img[pos[0] + a][pos[1] + 1]

    sum_diagonal += img[pos[0] - 1][pos[1]]
    average_diagonal = sum_diagonal / 3
    return average_diagonal

def diagonal_bottom_left(pos, img):
    list = [0, 1]
    sum_diagonal = 0
    average_diagonal = 0
    for a in list:
        sum_diagonal += img[pos[0] + a][pos[1] - 1]

    sum_diagonal += img[pos[0] + 1][pos[1]]
    average_diagonal = sum_diagonal / 3
    return average_diagonal

def diagonal_bottom_right(pos, img):
    list = [0, 1]
    sum_diagonal = 0
    average_diagonal = 0
    for a in list:
        sum_diagonal += img[pos[0] + a][pos[1] + 1]

    sum_diagonal += img[pos[0] + 1][pos[1]]
    average_diagonal = sum_diagonal / 3
    return average_diagonal
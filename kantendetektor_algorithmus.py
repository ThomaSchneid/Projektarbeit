from check_neighbours import *
from bild_einlesen import *

def oben_unten(img):
    x_limit = img.shape[1] - 1
    y_limit = img.shape[0] - 1
    pos = (1,1)
    print('top', top(pos, img))
    print('bottom', bottom(pos, img))
    print('left', left(pos, img))
    print('right', right(pos, img))
    print('diagonal_top_right', diagonal_top_right(pos, img))
    print('diagonal_top_left', diagonal_top_left(pos, img))
    print('diagonal_bottom_left', diagonal_bottom_left(pos, img))
    print('diagonal_bottom_right', diagonal_bottom_right(pos, img))

def direction(pos, img):
    oben_unten(img)
    direction = np.zeros((3,3))
    direction[0][0] = diagonal_top_left(pos, img) - diagonal_bottom_right(pos, img)
    direction[0][1] = top(pos, img) - bottom(pos, img)
    direction[0][2] = diagonal_top_right(pos, img) - diagonal_bottom_left(pos, img)
    direction[1][0] = left(pos, img) - right(pos, img)
    direction[1][2] = - direction[1][0]
    direction[2][0] = - direction[0][2]
    direction[2][1] = - direction[0][1]
    direction[2][2] = - direction[0][0]
    print('direction', direction)

    min = np.where(direction == np.amin(direction))
    print('min', min)
    result = list(zip(min[0], min[1]))
    print('result', result)
    direct = (result[0][0], result[0][1])
    print('direct', direct)
    return direct

def check_next_pixel(pos, img):
    y = img.shape[0]
    x = img.shape[1]
    direct = direction(pos, img)
    # check if next pixel should go up
    if direct[0] == 0:
        # check if we are at the top border
        if pos[0] != 0:
            if direct[1] == 0:
                next = (pos[0] - 1, pos[1] - 1)
            elif direct[1] == 1:
                next = (pos[0] - 1, pos[1])
            else:
                next = (pos[0] - 1, pos[1] + 1)
        # if we are at the top border try to go left
        elif pos[1] != 0:
            next = (pos[0], pos[1] - 1)
        # if we are also the the left border go down
        else:
            next = (pos[0] + 1, pos[1])
    # check if next pixel should be left or right
    elif direct[0] == 1:
        # just check if we are at the left border, if yes go right
        if direct[1] == 0 and pos[1] != 0:
            next = (pos[0], pos[1] - 1)
        else:
            next = (pos[0], pos[1] + 1)
    # if no case matched the direction has to be downwards
    else:
        # check if we are at the bottom border
        if pos[0] < y:
            if direct[1] == 0:
                next = (pos[0] + 1, pos[1] - 1)
            elif direct[1] == 1:
                next = (pos[0] + 1, pos[1])
            else:
                next = (pos[0] +1, pos[1] + 1)
        # if we are at the bottom border try to move left
        elif pos[1] != 0:
            next = (pos[0, pos[1] - 1])
        # if we are also at the left border move up
        else:
            next = (pos[0] + 1, pos[1])

    print('next', next)
    return next

oben_unten(japan())
direction((1,1), japan())

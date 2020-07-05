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
    print('direction',direction)

    min = np.where(direction == np.amin(direction))
    print('max',min)
    result = list(zip(min[0], min[1]))
    print('result', result)
    pos = (result[0][0], result[0][1])
    return direction, pos

oben_unten(japan())
direction((1,1), japan())

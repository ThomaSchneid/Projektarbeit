from check_neighbours import *
from bild_einlesen import *

# TODO - Matrix Klon erstellen und Mittelwert der jew. Richtungspixel eintragen

def direction(pos, img):
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
    return direction

def create_matrix(img):
    x_achse = img.shape[1]
    y_achse = img.shape[0]
    clone = np.zeros((y_achse, x_achse, 2))

    return img, y_achse, clone

def check_next_pixel(current_position, b):

    check_matrix = direction(current_position, b[0])

    min = np.where(check_matrix == np.amin(check_matrix))
    result = list(zip(min[0], min[1]))
    direct = (result[0][0], result[0][1])
    print('direct', direct)
    print('current_position', current_position)
    # check if next pixel should go up
    if direct[0] == 0:
        # check if we are at the top border
        if current_position[0] != 0:
            if direct[1] == 0:
                next_pixel_position = (current_position[0] - 1, current_position[1] - 1)
                b[2][current_position[0]][current_position[1]] = [check_matrix[0][0], 0]
            elif direct[1] == 1:
                next_pixel_position = (current_position[0] - 1, current_position[1])
                b[2][current_position[0]][current_position[1]] = [check_matrix[0][1], 1]
            else:
                next_pixel_position = (current_position[0] - 1, current_position[1] + 1)
                b[2][current_position[0]][current_position[1]] = [check_matrix[0][2], 2]
        # if we are at the top border try to go left
        elif current_position[1] != 0:
            next_pixel_position = (current_position[0], current_position[1] - 1)
            b[2][current_position[0]][current_position[1]] = [check_matrix[1][0], 3]
        # if we are also the the left border go down
        else:
            next_pixel_position = (current_position[0] + 1, current_position[1])
            b[2][current_position[0]][current_position[1]] = [check_matrix[2][1], 6]
    # check if next pixel should be left or right
    elif direct[0] == 1:
        # just check if we are at the left border, if yes go right
        if direct[1] == 0 and current_position[1] != 0:
            next_pixel_position = (current_position[0], current_position[1] - 1)
            b[2][current_position[0]][current_position[1]] = [check_matrix[1][0], 3]
        else:
            next_pixel_position = (current_position[0], current_position[1] + 1)
            b[2][current_position[0]][current_position[1]] = [check_matrix[1][2], 4]
    # if no case matched the direction has to be downwards
    else:
        # check if we are at the bottom border
        if current_position[0] < b[1]:
            if direct[1] == 0:
                next_pixel_position = (current_position[0] + 1, current_position[1] - 1)
                b[2][current_position[0]][current_position[1]] = [check_matrix[2][0], 5]
            elif direct[1] == 1:
                next_pixel_position = (current_position[0] + 1, current_position[1])
                b[2][current_position[0]][current_position[1]] = [check_matrix[2][1], 6]
            else:
                next_pixel_position = (current_position[0] +1, current_position[1] + 1)
                b[2][current_position[0]][current_position[1]] = [check_matrix[2][2], 7]
        # if we are at the bottom border try to move left
        elif current_position[1] != 0:
            next_pixel_position = (current_position[0, current_position[1] - 1])
            b[2][current_position[0]][current_position[1]] = [check_matrix[1][0], 3]
        # if we are also at the left border move up
        else:
            next_pixel_position = (current_position[0] + 1, current_position[1])
            b[2][current_position[0]][current_position[1]] = [check_matrix[0][1], 1]

    print('next_pixel_position', next_pixel_position)
    #print('clone', b[2])

    return next_pixel_position

x = 0
current_position = (1, 1)
b = create_matrix(japan())

while (x < 100):
    current_position = check_next_pixel(current_position, b)
    x += 1

print('x', x)
from check_neighbours import *
from bild_einlesen import *


def direction(pos, img):
    direction = np.zeros((3, 3))                        # matrix(zeilen, spalten)
    direction[0][2] = diagonal_top_right(pos, img) - diagonal_bottom_left(pos, img)
    direction[0][1] = top(pos, img) - bottom(pos, img)
    direction[0][0] = diagonal_top_left(pos, img) - diagonal_bottom_right(pos, img)
    direction[1][0] = left(pos, img) - right(pos, img)
    direction[2][0] = - direction[2][0]
    direction[2][1] = - direction[1][0]
    direction[2][2] = - direction[0][0]
    direction[1][2] = - direction[0][1]

    return direction


def create_matrix(img):
    global moving_direction_possibilities
    global forbidden_directions
    moving_direction_possibilities = [1,2,3,4,5,6,7,8]
    x_achse = img.shape[1]
    y_achse = img.shape[0]
    clone = np.zeros((y_achse, x_achse, 2))             # Aufbau Clone: (x,y,z)

    return img, y_achse, clone


# TODO: check if b[2][x][y][z] already has a value and respond according to it

def next_direction_to_move(current_position, y, direct):
    if direct[0] == 0:  # check for move up
        if current_position[0] != 0:  # check for top border
            moving_direction = direct[1] + 1
        elif current_position[1] != 0:  # move left cause we are at top border
            forbidden_directions.extend((1,2,3))
            moving_direction = 4
        else:  # move down if left border
            moving_direction = 7
            forbidden_directions.extend((1, 2, 3, 4))
    elif direct[0] == 1:  # check for left  or right
        if direct[1] == 0 and current_position[1] != 0:  # move right if left border
            moving_direction = 4
        else:
            moving_direction = 5
            forbidden_directions.extend(4)
    else:  # move down cause no case matches until now
        if current_position[0] < y:  # check for bottom border
            moving_direction = direct[1] + 6  # offset of 6 cause we need 6,7,8 instead of 1,2,3
        elif current_position[1] != 0:  # move left if bottom border
            moving_direction = 4
            forbidden_directions.extend((6, 7, 8))
        else:  # move up when also at left border
            moving_direction = 7
            forbidden_directions.extend((4, 6, 7, 8))

    return moving_direction

def position_of_next_pixel(moving_direction, current_position):
    if moving_direction == 1:
        next_pixel_position = (current_position[0] - 1, current_position[1] - 1)
    elif moving_direction == 2:
        next_pixel_position = (current_position[0] - 1, current_position[1])
    elif moving_direction == 3:
        next_pixel_position = (current_position[0] - 1, current_position[1] + 1)
    elif moving_direction == 4:
        next_pixel_position = (current_position[0], current_position[1] - 1)
    elif moving_direction == 5:
        next_pixel_position = (current_position[0], current_position[1] + 1)
    elif moving_direction == 6:
        next_pixel_position = (current_position[0] + 1, current_position[1] - 1)
    elif moving_direction == 7:
        next_pixel_position = (current_position[0] + 1, current_position[1])
    elif moving_direction == 8:
        next_pixel_position = (current_position[0] + 1, current_position[1] + 1)

    return next_pixel_position

def set_values_to_clone_matrix(moving_direction, current_position, clone, check_matrix, direct):
    clone[current_position][0] = check_matrix[direct]
    clone[current_position][1] = moving_direction

    return clone

def check_if_next_pixel_was_already_checked(moving_direction, clone, next_pixel_position):
    if clone[next_pixel_position][1] != 0:


    print('needs to be done, please give me functionality')


x = 0
current_position = (1, 1)
b = create_matrix(japan())
start = time.time()
clone = b[2]

while (x < 10):
    check_matrix = direction(current_position, b[0])
    min = np.where(check_matrix == np.amin(check_matrix))
    result = list(zip(min[0], min[1]))
    direct = (result[0][0], result[0][1])  # direct(zeile,spalte) from direction matrix
    moving_direction = next_direction_to_move(current_position, b[1], direct)
    clone = set_values_to_clone_matrix(moving_direction, current_position, clone, check_matrix, direct)
    print(clone)
    x += 1
    current_position = position_of_next_pixel(moving_direction, current_position)  # important for setting a new position

end = time.time()
time1 = end - start
print(time1)
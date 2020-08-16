from check_neighbours import *
from bild_einlesen import *

def direction(pos, img):

    direction = np.zeros((3, 3))
    direction[0][2] = abs(diagonal_top_right(pos, img) - diagonal_bottom_left(pos, img))
    direction[0][1] = abs(top(pos, img) - bottom(pos, img))
    direction[0][0] = abs(diagonal_top_left(pos, img) - diagonal_bottom_right(pos, img))
    direction[1][0] = abs(left(pos, img) - right(pos, img))
    direction[2][0] = value_raising_diagonal(pos, img)
    direction[2][1] = value_top_bottom(pos, img)
    direction[2][2] = value_falling_diagonal(pos, img)
    direction[1][2] = value_left_right(pos, img)
    return direction

def create_matrix(img):
    global forbidden_directions
    forbidden_directions = []
    x_achse = img.shape[1]
    y_achse = img.shape[0]
    clone = np.zeros((y_achse, x_achse, 2))

    return img, y_achse, clone

def next_direction_to_move(current_position, y, direct):
    if (direct[0] == 0) and (not all(k in forbidden_directions for k in (1, 2, 3))):  # check for move up
        if (current_position[0] != 0) and (1 not in forbidden_directions):  # check for top border
            moving_direction = 1
        elif (current_position[0] != 0) and (2 not in forbidden_directions):  # check for top border
            moving_direction = 2
        elif (current_position[0] != 0) and (3 not in forbidden_directions):  # check for top border
            moving_direction = 3
        elif (current_position[1] != 0) and (4 not in forbidden_directions):  # move left cause we are at top border
            forbidden_directions.extend((1, 2, 3))
            moving_direction = 4
        elif 7 not in forbidden_directions:  # move down if left border
            moving_direction = 7
            forbidden_directions.extend((1, 2, 3, 4))
        else:
            print("no case for moving_direction left")
            moving_direction = 9
    elif (direct[0] == 1) and (not all(k in forbidden_directions for k in (4, 5))):  # check for left  or right
        if (direct[1] == 0) and (current_position[1] != 0) and (4 not in forbidden_directions):  # move right if left border
            moving_direction = 4
        elif 5 not in forbidden_directions:
            moving_direction = 5
            forbidden_directions.append(4)
        else:
            print("no case for moving_direction left")
            moving_direction = 9
    else:  # move down cause no case matches until now
        if (current_position[0] < y) and (6 not in forbidden_directions):  # check for bottom border
            moving_direction = 6
        elif (current_position[0] < y) and (7 not in forbidden_directions):  # check for bottom border
            moving_direction = 7
        elif (current_position[0] < y) and (8 not in forbidden_directions):  # check for bottom border
            moving_direction = 8
        elif (current_position[1] != 0) and (4 not in forbidden_directions):  # move left if bottom border
            moving_direction = 4
            forbidden_directions.extend((6, 7, 8))
        elif 5 not in forbidden_directions:  # move right when also at left border
            moving_direction = 5
            forbidden_directions.extend((4, 6, 7, 8))
        else:
            print("no case for moving_direction left")
            moving_direction = 9

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
    elif moving_direction == 9:
        print("no_next_pixel_position")
        next_pixel_position = "moving in circles"

    return next_pixel_position

def set_values_to_clone_matrix(moving_direction, current_position, clone, direction_matrix, direct):
    clone[current_position][0] = direction_matrix[direct]
    clone[current_position][1] = moving_direction

    return clone

def check_if_next_pixel_was_already_checked(moving_direction, clone, next_pixel_position):
    if clone[next_pixel_position][1] != 0:
        print('needs to be done, please give me functionality')


x = 0
current_position = (1, 1)
b = create_matrix(japan())  #b[0] = image, b[1] = y-achse, b[2] = clone
#current_position = get_starting_point(b[0], b[1])
start = time.time()
clone = b[2]
all_moving_directions = []
all_positions = []

while (x < 10):
    direction_matrix = direction(current_position, b[0])
    min = np.where(direction_matrix == np.amin(direction_matrix))
    result = list(zip(min[0], min[1]))
    direct = (result[0][0], result[0][1])  # direct(zeile,spalte) from direction matrix
    moving_direction = next_direction_to_move(current_position, b[1], direct)
    clone = set_values_to_clone_matrix(moving_direction, current_position, clone, direction_matrix, direct)
    print(clone)
    temp_current_position = position_of_next_pixel(moving_direction, current_position)  # important for setting a new position

    # check next pixel
    while (clone[temp_current_position][1] != 0):
        if moving_direction == 9:
            print("moving in circles detected")
            clone[temp_current_position][1] = 0

        forbidden_directions.append(moving_direction)
        moving_direction = next_direction_to_move(current_position, b[1], direct)

    x += 1
    forbidden_directions = []
    current_position = temp_current_position


end = time.time()
time1 = end - start
print(time1)
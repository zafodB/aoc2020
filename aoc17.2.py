import copy

def open_file(location:str='17.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> list:
    cubes_input = [[[]]]
    for line in lines:
        cubes_input[0][0].append(list(line.replace('\n', '')))
    
    return cubes_input


# Make sure the field is big anough. Enlarge it if necessary
def prepare_field(state: list) -> list:
    # In part 2 of Day 17, skip checking, but always enlarge
    return enlarge_field(state)

# NOT UPDATED
# Find directions to extend (if there is an active cube at the current edge)
# def find_if_extension_needed(state:list):
    """
    Input: current state of field.

    Return: x, y, z integers: 1 if expansion in positive direction is needed, -1 if expansion
            in negative direction is needed
    """
    # expansion_dimensions: x+ x- y+ y- z+ z-
    expansion_dimensions = [False, False, False, False, False, False]


    # z axis (+)
    for y_row in state[0]:
        for x_cube in y_row:
            if x_cube == '#':
                expansion_dimensions[4] = True
                break
        
        if expansion_dimensions[4]:
            break
    
    # z axis (-)
    for y_row in state[-1]:
        for x_cube in y_row:
            if x_cube == '#':
                expansion_dimensions[5] = True
                break
        
        if expansion_dimensions[5] == True:
            break

    # y axis (+)
    for z_plane in state:
        for x_cube in z_plane[0]:
            if x_cube == '#':
                expansion_dimensions[2] = True
                break
        
        if expansion_dimensions[2] == True:
            break
    
    # y asix (-)
    for z_plane in state:
        for x_cube in z_plane[-1]:
            if x_cube == '#':
                expansion_dimensions[3] = True
                break
        
        if expansion_dimensions[3] == True:
            break
    
    # x asix (-)
    for z_plane in state:
        for y_row in z_plane:
            if y_row[0] == '#':
                expansion_dimensions[1] = True
                break
        
        if expansion_dimensions[1] == True:
            break
    
    # x asix (+)
    for z_plane in state:
        for y_row in z_plane:
            if y_row[-1] == '#':
                expansion_dimensions[0] = True
                break
        
        if expansion_dimensions[0] == True:
            break

    return tuple(expansion_dimensions)

# Enlarge the field according to instructions
def enlarge_field(state: list) -> list:
    updated_state = copy.deepcopy(state)

    # X +
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            for index_y, y_row in enumerate(z_plane):
                updated_state[index_w][index_z][index_y] = y_row + ['.']

    # X -
    state = copy.deepcopy(updated_state)
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            for index_y, y_row in enumerate(z_plane):
                updated_state[index_w][index_z][index_y] = ['.'] + y_row

    # Y -
    state = copy.deepcopy(updated_state)
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            updated_state[index_w][index_z] = [new_y_row] + updated_state[index_w][index_z]

    # Y +
    state = copy.deepcopy(updated_state)
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            updated_state[index_w][index_z] = updated_state[index_w][index_z] + [new_y_row]

    # Z -
    state = copy.deepcopy(updated_state)
    for index_w, w_space in enumerate(state):
        new_z_plane = []
        for index_z in range(len(state[0][0])):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            new_z_plane.append(new_y_row)

        updated_state[index_w] = [new_z_plane] + updated_state[index_w]        

    # Z +
    state = copy.deepcopy(updated_state)
    for index_w, w_space in enumerate(state):
        new_z_plane = []
        for index_z in range(len(state[0][0])):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            new_z_plane.append(new_y_row)

        updated_state[index_w] = updated_state[index_w] + [new_z_plane]

    # W -
    state = copy.deepcopy(updated_state)
    new_w_space = []
    for index_w in range(len(state[0])):
        new_z_plane = []
        for index_z in range(len(state[0][0])):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            new_z_plane.append(new_y_row)
        new_w_space.append(new_z_plane)
  
    updated_state = [new_w_space] + updated_state

    # W +
    state = copy.deepcopy(updated_state)
    new_w_space = []
    for index_w in range(len(state[0])):
        new_z_plane = []
        for index_z in range(len(state[0][0])):
            new_y_row = ['.' for _ in range(len(state[0][0][0]))]
            new_z_plane.append(new_y_row)        
        new_w_space.append(new_z_plane)
    
    updated_state = updated_state + [new_w_space]


    return updated_state


# Check how many surrouding cells are active
def check_active_neighbours(state, x, y, z, w) -> int:
    active_neighbours = 0

    for index_w in range(-1,2,1):
        if (index_w == -1 and w == 0) or (index_w == 1 and w == len(state) -1):
            continue
        else:
            for index_z in range(-1,2,1):
                if (index_z == -1 and z == 0) or (index_z == 1 and z == len(state[0]) -1):
                    continue
                else:
                    for index_y in range(-1, 2, 1):
                        if (index_y == -1 and y == 0) or (index_y == 1 and y == len(state[0][0]) -1):
                            continue
                        else:
                            for index_x in range(-1, 2, 1):
                                # print(f"w: {index_w+w}, z: {index_z+z}, y: {index_y+y}, x:{index_x+x}")
                                # print(f"dimensions: w: {len(state)}, z: {len(state[0])}, y: {len(state[0][0])}, x:{len(state[0][0][0])}")

                                if (index_x == -1 and x == 0) or (index_x == 1 and x == len(state[0][0][0]) -1):
                                    continue
                                # Do not count self
                                elif index_x == index_y == index_z == index_w == 0:
                                    continue
                                elif state[w+index_w][z+index_z][y+index_y][x+index_x] == '#':
                                    active_neighbours += 1

    return active_neighbours
    

def play_round(state: list) -> list:
    new_state = copy.deepcopy(state)

    print(f'Dimensions w:{len(state)}, z:{len(state[0])}, y:{len(state[0][0])}, x:{len(state[0][0][0])}')
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            for index_y, y_row in enumerate(z_plane):
                for index_x, x_cube in enumerate(y_row):
                    active = check_active_neighbours(state, index_x, index_y, index_z, index_w)
                    if x_cube == '.' and active == 3:
                        new_state[index_w][index_z][index_y][index_x] = '#'
                    elif x_cube == '#' and active >= 2 and active <= 3:
                        new_state[index_w][index_z][index_y][index_x] = '#'
                    else:
                        new_state[index_w][index_z][index_y][index_x] = '.'

    return new_state


updated_state = process_input(open_file())
# updated_state = process_input(open_file('17.1.input.test2.txt'))
# updated_state = process_input(open_file('17.1.input.test.txt'))

def plane_print(state):
    print('Printing')
    for index_w, w_space in enumerate(state):
        for index_z, z_plane in enumerate(w_space):
            print(f'w: {index_w}, z: {index_z}')
            for row in z_plane:
                print(row)
            
            print()

def count_active(state: list) -> int:
    active_cubes = 0
    for w_space in state:
        for z_plane in w_space:
            for y_row in z_plane:
                for x_cube in y_row:
                    if x_cube == '#':
                        active_cubes += 1
        
    return active_cubes


# plane_print(updated_state)
for round_number in range(6):
    
    updated_state = play_round(prepare_field(updated_state))
    print(f'Round: {round_number}, active: {count_active(updated_state)}, dimensions: x:{len(updated_state[0][0][0])}, y:{len(updated_state[0][0])}, z:{len(updated_state[0])}, w:{len(updated_state)}')

    # plane_print(updated_state)

print(count_active(updated_state))
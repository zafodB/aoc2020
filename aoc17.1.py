import copy

def open_file(location:str='17.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> list:
    cubes_input = [[]]
    for line in lines:
        cubes_input[0].append(list(line.replace('\n', '')))
    
    return cubes_input

# Make sure the field is big anough. Enlarge it if necessary
def prepare_field(state: list) -> list:
    extension_dimensions = find_if_extension_needed(state)

    if any(extension_dimensions):
        new_field = enlarge_field(state, extension_dimensions)
        return new_field
    else:
        return state

# Find directions to extend (if there is an active cube at the current edge)
def find_if_extension_needed(state:list):
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
def enlarge_field(state: list, dimensions: (bool, bool, bool, bool, bool, bool)) -> list:

    updated_state = copy.deepcopy(state)

    # new z plane -
    if dimensions[5]:
        new_z_plane = []
        for y_row in range(len(state[0])):
            new_z_plane.append(['.' for _ in range(len(state[0][0]))])
        
        updated_state = updated_state + [new_z_plane]

    state = copy.deepcopy(updated_state)
    # new z plane +
    if dimensions[4]:
        new_z_plane = []
        for y_row in range(len(state[0])):
            new_z_plane.append(['.' for _ in range(len(state[0][0]))])

        updated_state = [new_z_plane] + updated_state

    state = copy.deepcopy(updated_state)
    # new y plane -
    if dimensions[3]:
        for index, z_plane in enumerate(state):
            updated_state[index] = updated_state[index] + [['.' for _ in range(len(state[0][0]))]]

    state = copy.deepcopy(updated_state)
    # new y plane +
    if dimensions[2]:
        for index, z_plane in enumerate(state):
            updated_state[index] = [['.' for _ in range(len(state[0][0]))]] + updated_state[index]

    state = copy.deepcopy(updated_state)
    # new x plane -
    if dimensions[1]:
        for index_z, z_plane in enumerate(state):
            for index_y, y_row in enumerate(z_plane):
                updated_state[index_z][index_y] = ['.'] + updated_state[index_z][index_y]

    state = updated_state.copy()

    # new x plane +
    if dimensions[0]:
        for index_z, z_plane in enumerate(state):
            for index_y, y_row in enumerate(z_plane):
                updated_state[index_z][index_y] = updated_state[index_z][index_y] + ['.']

    return updated_state

# Check how many surrouding cells are active
def check_active_neighbours(state, x, y, z) -> int:
    active_neighbours = 0

    for index_z in range(-1,2, 1):
        if (index_z == -1 and z == 0) or (index_z == 1 and z == len(state) -1):
            continue
        else:
            for index_y in range(-1, 2, 1):
                if (index_y == -1 and y == 0) or (index_y == 1 and y == len(state[0]) -1):
                    continue
                else:
                    for index_x in range(-1, 2, 1):
                        if (index_x == -1 and x == 0) or (index_x == 1 and x == len(state[0][0]) -1):
                            continue
                        elif index_x == index_y == index_z == 0:
                            continue
                        elif state[z+index_z][y+index_y][x+index_x] == '#':
                            active_neighbours += 1

    return active_neighbours
    

def play_round(state: list) -> list:
    new_state = copy.deepcopy(state)

    for index_z, z_plane in enumerate(state):
        for index_y, y_row in enumerate(z_plane):
            for index_x, x_cube in enumerate(y_row):
                active = check_active_neighbours(state, index_x, index_y, index_z)
                if x_cube == '.' and active == 3:
                    new_state[index_z][index_y][index_x] = '#'
                elif x_cube == '#' and active >= 2 and active <= 3:
                    new_state[index_z][index_y][index_x] = '#'
                else:
                    new_state[index_z][index_y][index_x] = '.'

    return new_state


updated_state = process_input(open_file())
# updated_state = process_input(open_file('17.1.input.test2.txt'))
# updated_state = process_input(open_file('17.1.input.test.txt'))

def plane_print(state):
    print('Printing')
    for index, z_plane in enumerate(state):
        # print(f'z: {index}')
        for row in z_plane:
            print(row)
        
        print()

def count_active(state: list) -> int:
    active_cubes = 0
    for z_plane in state:
        for y_row in z_plane:
            for x_cube in y_row:
                if x_cube == '#':
                    active_cubes += 1
    
    return active_cubes


plane_print(updated_state)

for round_number in range(6):
    
    updated_state = play_round(prepare_field(updated_state))
    print(f'Round: {round_number}, active: {count_active(updated_state)}, dimensions: x:{len(updated_state[0][0])}, y:{len(updated_state[0])}, z:{len(updated_state)}')

    plane_print(updated_state)

# plane_print(updated_state)
print(count_active(updated_state))
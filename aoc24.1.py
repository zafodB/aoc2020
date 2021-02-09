from collections import deque

EAST = 'ex'
SOUTH_EAST = 'se'
SOUTH_WEST = 'sw'
WEST = 'wx'
NORTH_WEST = 'nw'
NORTH_EAST = 'ne'
BLACK, WHITE = True, False


def open_file(location:str='24.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> list:
    directions = []
    for line in lines:
        tile_location = []

        line_queue = deque(line.replace('\n', ''))
        while line_queue:
            
            if len(line_queue) > 1 and (line_queue[0] + line_queue[1]) == 'se':
                tile_location.append(SOUTH_EAST)
                line_queue.popleft()
                line_queue.popleft()

            elif len(line_queue) > 1 and (line_queue[0] + line_queue[1]) == 'ne':
                tile_location.append(NORTH_EAST)
                line_queue.popleft()
                line_queue.popleft()

            elif len(line_queue) > 1 and (line_queue[0] + line_queue[1]) == 'sw':
                tile_location.append(SOUTH_WEST)
                line_queue.popleft()
                line_queue.popleft()

            elif len(line_queue) > 1 and (line_queue[0] + line_queue[1]) == 'nw':
                tile_location.append(NORTH_WEST)
                line_queue.popleft()
                line_queue.popleft()

            else:
                direction = line_queue.popleft()
                if direction == 'e':
                    tile_location.append(EAST)
                else:
                    tile_location.append(WEST)

        directions.append(tile_location)   
        
    return directions
            

tile_plan = process_input(open_file())
# tile_plan = process_input(open_file('24.1.input.test.txt'))

floor_state = {0: {0: WHITE}}

for instruction in tile_plan:
    # x, y
    current_position = [0, 0]

    for direction in instruction:
        if direction == EAST:
            current_position[0] += 1

        elif direction == SOUTH_EAST:
            if current_position[1] % 2 == 1:
                current_position[0] += 1

            current_position[1] += 1

        elif direction == SOUTH_WEST:
            if current_position[1] % 2 == 0:
                current_position[0] -= 1
                
            current_position[1] += 1

        elif direction == WEST:
            current_position[0] -= 1

        elif direction == NORTH_EAST:
            if current_position[1] % 2 == 1:
                current_position[0] += 1
                
            current_position[1] -= 1

        elif direction == NORTH_WEST:
            if current_position[1] % 2 == 0:
                current_position[0] -= 1
                
            current_position[1] -= 1
    
    if current_position[0] not in floor_state:
        floor_state[current_position[0]] = {}
    
    if current_position[1] not in floor_state[current_position[0]]:
        floor_state[current_position[0]][current_position[1]] = WHITE

    floor_state[current_position[0]][current_position[1]] = not floor_state[current_position[0]][current_position[1]]

black_tile_counter = 0
for row in floor_state.values():
    for tile in row.values():
        if tile:
            black_tile_counter += 1

print(black_tile_counter)
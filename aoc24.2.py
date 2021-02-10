import json
from collections import deque
from tqdm import tqdm

EAST = 'ex'
SOUTH_EAST = 'se'
SOUTH_WEST = 'sw'
WEST = 'wx'
NORTH_WEST = 'nw'
NORTH_EAST = 'ne'
BLACK, WHITE = True, False

# with open('24.2.test.input.json', 'r') as input_file:
with open('24.2.input.json', 'r') as input_file:
    floor_map = json.load(input_file)

def count_black_tiles(floor_map: deque) -> int:
    black_tile_counter = 0
    for row in floor_map:
        for tile in row:
            if tile:
                black_tile_counter += 1
    
    return black_tile_counter


def convert_to_deques(floor_map: dict) -> deque:
    # Find Max dimensions
    max_x, min_x, max_y, min_y = 0, 0, 0, 0

    for column_string in floor_map:
        column = int(column_string)
        if column > max_x:
            max_x = column
        if column < min_x:
            min_x = column
        for row_string in floor_map[column_string]:
            row = int(row_string)
            if row > max_y:
                max_y = row
            if row < min_y:
                min_y = row

    # Convert to deque with max dimensions
    floor_field = deque()
    for x in range(min_x, max_x + 1):
        new_column = deque()

        for y in range(min_y, max_y + 1):
            try:
                new_column.append(floor_map[str(x)][str(y)])
            except KeyError:
                new_column.append(WHITE)

        floor_field.append(new_column)
    
    return floor_field


def expand_field(old_field: deque) -> deque:
    empty_column = deque([WHITE for _ in old_field[0]])
    extended_field = deque()
    extended_field.append(empty_column.copy())
    extended_field.append(empty_column.copy())
    [extended_field.append(col) for col in old_field]
    extended_field.append(empty_column.copy())
    extended_field.append(empty_column.copy())

    for i in range(len(extended_field)):
        extended_field[i].appendleft(WHITE)
        extended_field[i].appendleft(WHITE)
        extended_field[i].append(WHITE)
        extended_field[i].append(WHITE)

    return extended_field


def find_active_around(field: deque, tile_x: int, tile_y: int) -> int:
    active_count = 0
    
    # west
    if tile_x > 0 and field[tile_x-1][tile_y]:
        active_count += 1
    
    # east
    if tile_x < len(field)-1 and field[tile_x+1][tile_y]:
        active_count += 1
    
    # north west
    if tile_y > 0:
        if tile_y % 2 == 1:
            if tile_x > 0:
                if field[tile_x-1][tile_y-1]:
                    active_count += 1
        else:
            if field[tile_x][tile_y-1]:
                active_count += 1

    # north east
    if tile_y > 0:
        if tile_y % 2 == 1:
                if field[tile_x][tile_y-1]:
                    active_count += 1
        else:
            if tile_x < len(field)-1:
                if field[tile_x+1][tile_y-1]:
                    active_count += 1

    # south west
    if tile_y < len(field[tile_x]) - 1:
        if tile_y % 2 == 1:
            if tile_x > 0:
                if field[tile_x-1][tile_y+1]:
                    active_count += 1
        else:
            if field[tile_x][tile_y+1]:
                active_count += 1

    # south east
    if tile_y < len(field[tile_x]) -1:
        if tile_y % 2 == 1:
                if field[tile_x][tile_y+1]:
                    active_count += 1
        else:
            if tile_x < len(field)-1:
                if field[tile_x+1][tile_y+1]:
                    active_count += 1
    
    return active_count


def play_round(field: deque) -> deque:
    updated_field = deque()

    for index_x, col in enumerate(field):
        new_column = deque()
        for index_y, tile in enumerate(col):
            active_fields = find_active_around(field, index_x, index_y)

            if tile is BLACK:
                if active_fields < 1 or active_fields > 2:
                    new_column.append(WHITE)
                else:
                    new_column.append(BLACK)
            else:
                if active_fields == 2:
                    new_column.append(BLACK)
                else:
                    new_column.append(WHITE)                    
        
        updated_field.append(new_column)

    return updated_field

def print_field(field_to_print):
    for column in field_to_print:
        print([int(v) for v in column])


floor_field = convert_to_deques(floor_map)
print_field(floor_field)

floor_field = expand_field(floor_field)

print(count_black_tiles(floor_field))

for i in tqdm(range(100)):
    floor_field = expand_field(floor_field)
    floor_field = play_round(floor_field)

print(count_black_tiles(floor_field))
def open_file(location:str='11.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: dict) -> dict:
    processed_input = []
    for line in lines:
        processed_input.append(line.replace("\n", ''))
    
    return processed_input

def look_up_left(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == 0 or seat_index == 0:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index - i < 0 or seat_index - i < 0:
            return 0
        
        if seat_map[row_index - i][seat_index - i] == 'L':
            return 0
        
        if seat_map[row_index - i][seat_index - i] == '#':
            return 1


def look_up(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == 0:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index - i < 0:
            return 0
        
        if seat_map[row_index - i][seat_index] == 'L':
            return 0
        
        if seat_map[row_index - i][seat_index] == '#':
            return 1

def look_up_right(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == 0 or seat_index == seats_total:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index - i < 0 or seat_index + i > seats_total:
            return 0
        
        if seat_map[row_index - i][seat_index + i] == 'L':
            return 0
        
        if seat_map[row_index - i][seat_index + i] == '#':
            return 1

def look_left(seat_map, row_index, seat_index, rows_total, seats_total):
    if seat_index == 0:
        return 0
    
    i = 0
    while True:
        i += 1
        if seat_index - i < 0:
            return 0
        
        if seat_map[row_index][seat_index - i] == 'L':
            return 0
        
        if seat_map[row_index][seat_index - i] == '#':
            return 1

def look_right(seat_map, row_index, seat_index, rows_total, seats_total):
    if seat_index == seats_total:
        return 0
    
    i = 0
    while True:
        i += 1
        if seat_index + i > seats_total:
            return 0
        
        if seat_map[row_index][seat_index + i] == 'L':
            return 0
        
        if seat_map[row_index][seat_index + i] == '#':
            return 1

def look_down_left(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == rows_total or seat_index == 0:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index + i > rows_total or seat_index - i < 0:
            return 0
        
        if seat_map[row_index + i][seat_index - i] == 'L':
            return 0
        
        if seat_map[row_index + i][seat_index - i] == '#':
            return 1

def look_down(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == rows_total:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index + i > rows_total:
            return 0
        
        if seat_map[row_index + i][seat_index] == 'L':
            return 0
        
        if seat_map[row_index + i][seat_index] == '#':
            return 1

def look_down_right(seat_map, row_index, seat_index, rows_total, seats_total):
    if row_index == rows_total or seat_index == seats_total:
        return 0
    
    i = 0
    while True:
        i += 1
        if row_index + i > rows_total or seat_index + i > seats_total:
            return 0
        
        if seat_map[row_index + i][seat_index + i] == 'L':
            return 0
        
        if seat_map[row_index + i][seat_index + i] == '#':
            return 1

def check_around_free(seat_map, row_index, seat_index, rows_total, seats_total):
    occupied = 0

    # Up left
    occupied += look_up_left(seat_map, row_index, seat_index, rows_total, seats_total)

    # Up middle
    occupied += look_up(seat_map, row_index, seat_index, rows_total, seats_total)

    # Up right
    occupied += look_up_right(seat_map, row_index, seat_index, rows_total, seats_total)

    # same left
    occupied += look_left(seat_map, row_index, seat_index, rows_total, seats_total)

    # same right
    occupied += look_right(seat_map, row_index, seat_index, rows_total, seats_total)

    # bottom left 
    occupied += look_down_left(seat_map, row_index, seat_index, rows_total, seats_total)

    # bottom middle
    occupied += look_down(seat_map, row_index, seat_index, rows_total, seats_total)
   
    # bottom right
    occupied += look_down_right(seat_map, row_index, seat_index, rows_total, seats_total)
    
    return occupied



seat_map = process_input(open_file())
# seat_map = process_input(open_file(location='11.1.input.test.txt'))

total_rows = len(seat_map) - 1
seats_per_row = len(seat_map[0]) - 1

print(f'rows: {total_rows}, seats: {seats_per_row}')

# print(f"dimensions start: {len(seat_map)} {len(seat_map[0])}")

change = True
round = 0

while change:
    round += 1
    print(f"updating, round: {round}. Current state:")

    # for row in seat_map:
    #     print(row)

    updated_map = []
    for row_index, row in enumerate(seat_map):
        updated_row = ""

        for seat_index, seat in enumerate(row):
           
            if seat == 'L' and check_around_free(seat_map, row_index, seat_index, total_rows, seats_per_row) == 0:
                updated_row = updated_row + "#"
            elif seat == '#' and check_around_free(seat_map, row_index, seat_index, total_rows, seats_per_row) >= 5:
                updated_row = updated_row + "L"
            else:
                updated_row = updated_row + seat

        updated_map.append(updated_row)

    change = False

    for index, row in enumerate(seat_map):
        if row != updated_map[index]:
            change = True

            seat_map = updated_map.copy()
            break

seat_map = updated_map

# print(f"dimensions end: {len(seat_map)} {len(seat_map[0])}")

total_occupied_seats = 0

for row in seat_map:
    print(row)
    for seat in row:
        if seat == "#":
            total_occupied_seats += 1
 

print(total_occupied_seats)
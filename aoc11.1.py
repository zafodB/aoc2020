def open_file(location:str='11.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: dict) -> dict:
    processed_input = []
    for line in lines:
        processed_input.append(line.replace("\n", ''))
    
    return processed_input

def check_around_free(seat_map, row_index, seat_index, rows_total, seats_total):
    occupied = 0


    # if seat_index + 1 > seats_total:
    #     seat_index = None
    # elif seat_index - 1 < 0:
    #     seat_index = None

    # if row_index + 1 > rows_total:
    #     row_index = None
    # elif row_index - 1 < 0:
    #     row_index = None

    # Up left
    if not row_index - 1 < 0 and not seat_index - 1 < 0 and seat_map[row_index - 1][seat_index - 1] == "#":
        occupied += 1

    # Up middle
    if not row_index - 1 < 0 and seat_map[row_index - 1][seat_index] == "#":
        occupied += 1

    # Up right
    if not row_index - 1 < 0 and not seat_index + 1 > seats_total and seat_map[row_index - 1][seat_index + 1] == "#":
        occupied += 1

    # same left
    if not seat_index - 1 < 0 and seat_map[row_index][seat_index - 1] == "#":
        occupied += 1

    # same right
    if not seat_index + 1 > seats_total and seat_map[row_index][seat_index + 1] == "#":
        occupied += 1

    # bottom left 
    if not row_index + 1 > rows_total and not seat_index - 1 < 0 and seat_map[row_index + 1][seat_index - 1] == "#":
        occupied += 1

    # bottom middle
    if not row_index + 1 > rows_total and seat_map[row_index + 1][seat_index] == "#":
        occupied += 1
   
    # bottom right
    if not row_index + 1 > rows_total and not seat_index + 1 > seats_total and seat_map[row_index + 1][seat_index + 1] == "#":
        occupied += 1
    
    return occupied


seat_map = process_input(open_file())

total_rows = len(seat_map) - 1
seats_per_row = len(seat_map[0]) - 1

print(f'rows: {total_rows}, seats: {seats_per_row}')

# print(f"dimensions start: {len(seat_map)} {len(seat_map[0])}")

change = True
round = 0

while change:
    round += 1
    print(f"updating, round: {round}. Current state:")

    for row in seat_map:
        print(row)

    updated_map = []
    for row_index, row in enumerate(seat_map):
        updated_row = ""

        for seat_index, seat in enumerate(row):
           
            if seat == 'L' and check_around_free(seat_map, row_index, seat_index, total_rows, seats_per_row) == 0:
                updated_row = updated_row + "#"
            elif seat == '#' and check_around_free(seat_map, row_index, seat_index, total_rows, seats_per_row) >= 4:
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
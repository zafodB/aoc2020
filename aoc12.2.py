def open_file(location:str='12.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> list:
    processed_input = []
    for line in lines:
        processed_input.append((line[0], int(line[1:].replace('\n', ''), base=10)))
    
    return processed_input


instructions = process_input(open_file())
# instructions = process_input(open_file('12.1.input.test.txt'))

ship_x, ship_y = 0, 0
waypoint_x, waypoint_y = 10, 1

for item in instructions:
    if item[0] == 'N':
        waypoint_y += item[1]
    elif item[0] == 'S':
        waypoint_y -= item[1]
    elif item[0] == 'W':
        waypoint_x -= item[1]
    elif item[0] == 'E':
        waypoint_x += item[1]
    elif item[0] == 'L':
        print(item[1])
        for _ in range((item[1] // 90) % 4):
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    elif item[0] == 'R':
        print(item[1])
        for _ in range((item[1] // 90) % 4):
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x
    elif item[0] == 'F':
        ship_x += item[1]*waypoint_x
        ship_y += item[1]*waypoint_y

    # print(f'waypoint location x: {waypoint_x}, y: {waypoint_y}')
    # print(f'ship location x: {ship_x}, y: {ship_y}')

print(f"\nShip's location: x: {ship_x}, y: {ship_y}. Manhattan distance: {abs(ship_x)+abs(ship_y)}")
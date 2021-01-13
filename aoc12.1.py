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

x, y = 0, 0
heading = 90

for item in instructions:
    if item[0] == 'N':
        y -= item[1]
    elif item[0] == 'S':
        y += item[1]
    elif item[0] == 'W':
        x -= item[1]
    elif item[0] == 'E':
        x += item[1]
    elif item[0] == 'R':
        heading += item[1]
    elif item[0] == 'L':
        heading -= item[1]
    elif item[0] == 'F':
        if (heading / 90) % 4 == 0:
            # print('heading north')
            y -= item[1]
        elif (heading / 90) % 4 == 1:
            # print('heading east')
            x += item[1]
        elif (heading / 90) % 4 == 2:
            # print('heading south')
            y += item[1]
        elif (heading / 90) % 4 == 3:
            # print('heading west')
            x -= item[1]

print(f'x: {x}, y: {y}. Manhattan distance: {abs(x)+abs(y)}')
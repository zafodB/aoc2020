from collections import deque

# puzzle_input = '463528179' 
puzzle_input = '389125467' # test input

number_of_cups = 1000000

cup_circle = deque([int(_) for _ in puzzle_input])

for more_cup in range(10, 1000001):
    cup_circle.append(more_cup)

print(len(cup_circle))

def make_move(input_circle: deque, current_cup: int) -> deque:

    # print(f'Current circle: {input_circle}')

    current_cup_index = input_circle.index(current_cup)

    pick_three = []
    
    for i in range(3):
        pick_index = i + current_cup_index + 1
        if pick_index > number_of_cups - 1:
            pick_index -= number_of_cups

        pick_three.append(input_circle[pick_index])

    for cup in pick_three:
        input_circle.remove(cup)

    destination_cup = current_cup - 1
    if destination_cup < 1:
        destination_cup += number_of_cups

    while destination_cup in pick_three:
        destination_cup -= 1

        # wrap around
        if destination_cup < 1:
            destination_cup += number_of_cups

    destination_cup_index = input_circle.index(destination_cup)
    for cup in reversed(pick_three):
        input_circle.insert(destination_cup_index + 1 , cup)

    return input_circle


current_cup_value = cup_circle[number_of_cups - 1]

counter = 0
for number_of_moves in range(10000000):
    counter += 1

    if counter % 1000 == 0:
        print(f'Progress: {counter}')

    current_cup_index = cup_circle.index(current_cup_value)

    current_cup_index += 1
    if current_cup_index > number_of_cups - 1:
        current_cup_index -= number_of_cups
    
    current_cup_value = cup_circle[current_cup_index]

    cup_circle = make_move(cup_circle, current_cup_value)

index_of_cup_one = cup_circle.index(1)

print(f'RESULT: {cup_circle[index_of_cup_one+1]} and {cup_circle[index_of_cup_one+2]} \n')

# Submit answer starting from cup 1 clockwise
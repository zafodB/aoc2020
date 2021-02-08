from collections import deque

puzzle_input = '463528179' 
# puzzle_input = '389125467' # test input

cup_circle = deque([int(_) for _ in puzzle_input])

print(cup_circle)

def make_move(input_circle: deque, current_cup: int) -> deque:

    print(f'Current circle: {input_circle}')

    current_cup_index = input_circle.index(current_cup)

    pick_three = []
    
    for i in range(3):
        pick_index = i + current_cup_index + 1
        if pick_index > 8:
            pick_index -= 9

        pick_three.append(input_circle[pick_index])

    for cup in pick_three:
        input_circle.remove(cup)

    destination_cup = current_cup - 1
    if destination_cup < 1:
        destination_cup += 9

    while destination_cup in pick_three:
        destination_cup -= 1

        # wrap around
        if destination_cup < 1:
            destination_cup += 9

    destination_cup_index = input_circle.index(destination_cup)
    for cup in reversed(pick_three):
        input_circle.insert(destination_cup_index + 1 , cup)

    return input_circle


current_cup_value = cup_circle[8]

for number_of_moves in range(100):
    current_cup_index = cup_circle.index(current_cup_value)

    current_cup_index += 1
    if current_cup_index > 8:
        current_cup_index -= 9
    
    current_cup_value = cup_circle[current_cup_index]

    cup_circle = make_move(cup_circle, current_cup_value)

print(f'RESULT: {cup_circle}\n')

# Submit answer starting from cup 1 clockwise
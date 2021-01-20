
# puzzle_input = [1,3,2]
# puzzle_input = [2,1,3]
# puzzle_input = [1,2,3]
# puzzle_input = [2,3,1]
# puzzle_input = [0,3,6]
puzzle_input = [0,6,1,7,2,19,20]

number_ages = dict()

# iterations = 10 # test input
iterations = 2020 # day 1 variation
# iterations = 30000000 # day 2 variation

for i in range(iterations):
    if i % 1000000 == 0:
        print(f'Iteration: {i}')
    
    try:
        current_number = puzzle_input[i]
    except IndexError:
        if current_number in number_ages:
            if number_ages[current_number][0] is None:
                current_number = 0
            else:
                current_number = number_ages[current_number][1] - number_ages[current_number][0]

    if current_number not in number_ages:
         number_ages[current_number] = (None, i)
    else:
        last_mention = number_ages[current_number][1]
        number_ages[current_number] = (last_mention, i)
    
print(f'Number after {iterations} iterations is: {current_number}.')
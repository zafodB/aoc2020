def open_file(location:str='aoc9.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: dict) -> dict:
    processed_input = []
    for line in lines:
        processed_input.append(int(line.strip(), base=10))
    
    return processed_input

input_raw = open_file()
input_ready = process_input(input_raw)

master_number = 248131121
found_it = False

for index, number in reversed(list(enumerate(input_ready))):
    number_sum = number

    for second_index, number_b in reversed(list(enumerate(input_ready[0:index]))):
        number_sum += number_b

        if number_sum == master_number:
            found_it = True

            print(f"Index a: {index}, index b: {second_index}")
            break
        elif number_sum < master_number:
            continue
        else:
            break

    if found_it:
        break

    # 248 131 121
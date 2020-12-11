def open_file(location:str='10.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: dict) -> dict:
    processed_input = []
    for line in lines:
        processed_input.append(int(line.strip(), base=10))
    
    return processed_input

intpu_raw = open_file()
input_ready = process_input(intpu_raw)

numbers_as_set = set(input_ready)

difference_count = {1: 0, 2: 0, 3: 0}

numbers_as_list = list(numbers_as_set)

for index, number in enumerate(numbers_as_list):
    if index == 0:
        continue
    
    difference = number - numbers_as_list[index-1]

    difference_count[difference] += 1
    # print(difference)

print(difference_count)
# print(list(numbers_as_set))
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

for index, number in enumerate(input_ready):
    if index < 25:
        continue
    
    pair_found = False

    for prev_index, previous_number_a in reversed(list(enumerate(input_ready[index-25:index]))):
        for previous_number_b in reversed(input_ready[index-25:index-25+prev_index]):
            if previous_number_a + previous_number_b == number:
                pair_found = True
                break
        
        if pair_found:
            break
    
    if pair_found:
        continue
    else:
        print(f"Could not find pair for number {number}")
        break
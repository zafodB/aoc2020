import re

def open_file(location:str='14.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> list:
    instructions = []

    for line in lines:
        if line[:4] == 'mask':
            instructions.append(line[7:].replace('\n', ''))
            # print(line[7:].replace('\n', ''))
        elif line[:3] == 'mem':
            address = int(re.search(r"\[[0-9]*\]", line).group()[1:-1], base=10)
            value = int(line.split(' = ')[-1].replace('\n', ''), base=10)
            instructions.append((address, value))
    
    return instructions

instructions = process_input(open_file('14.1.input.txt'))
# instructions = process_input(open_file('14.1.input.test.txt'))

# print(instructions)

address_space = {}
current_mask = None

for instruction in instructions:
    if len(instruction) > 2 :
        current_mask = instruction
    if len(instruction) == 2:
        address = instruction[0]
        value = instruction[1]

        if not address in address_space:
            address_space[address] = 0

        for index, mask_bit in enumerate(reversed(current_mask)):
            if mask_bit == 'X':
                pass
            elif mask_bit == '0':
                value &= ~(1<<index)
            elif mask_bit == '1':
                value |= (1<<index)
        
        address_space[address] = value
    
grand_total = sum(address_space.values())
print(address_space)
print(grand_total)

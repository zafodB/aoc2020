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

instructions = process_input(open_file())
# instructions = process_input(open_file('14.2.input.test.txt'))

# print(instructions)

address_space = {}
current_mask = None

instruction_count = 0


for instruction in instructions:
    instruction_count += 1
    print(f'Now processing instruction: {instruction_count}')

    if len(instruction) > 2 :
        current_mask = instruction
    if len(instruction) == 2:
        # print(f'Now assignment instruction with mask: {current_mask}')

        base_address = instruction[0]
        # print(f'Original address: {base_address:b}')
        count_floating_bits = 0
        floating_bit_positions = []

        for index, mask_bit in enumerate(reversed(current_mask)):
            if mask_bit == '1':
                base_address |= (1<<index)
            elif mask_bit == 'X':
                count_floating_bits += 1
                base_address &= ~(1<<index)
                floating_bit_positions.append(index)
        

        if count_floating_bits > 0:
            possibilities = 2**count_floating_bits

        floating_addresses = []

        for i in range(possibilities):
            current_address = base_address

            for index, bit in enumerate(reversed(f'{i:b}')):
                if bit == '0':
                    current_address &= ~(1<<floating_bit_positions[index] )
                elif bit == '1':
                    current_address |= (1<<floating_bit_positions[index] )

            floating_addresses.append(current_address)

        for address in floating_addresses:
            if not address in address_space:
                address_space[address] = 0

            address_space[address] = instruction[1]
    
grand_total = sum(address_space.values())

# print(address_space)
print(grand_total)

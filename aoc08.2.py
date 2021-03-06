import json
import copy


def read_input(file_name: str = '8.1.input.txt') -> list:
    with open(file_name, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> dict:
    instructions = dict()

    for index, line in enumerate(lines):
        instruction = line[:3]
        value = int(line.strip()[4:], base=10)

        # print(instruction)
        # print(value)

        instructions[index] = [instruction, value, False]

    return instructions
    # print(instructions[5])


def execute_boot(instructions: dict):

    boot_counter = 0
    execute_next = 0

    while True:
        if instructions[execute_next][2] == True:
            break

        instructions[execute_next][2] = True

        if instructions[execute_next][0] == 'vic':
            print(f"Victorious! {boot_counter}")

            return execute_next

        elif instructions[execute_next][0] == 'nop':
            execute_next += 1
            continue
        elif instructions[execute_next][0] == 'acc':
            boot_counter += instructions[execute_next][1]
            execute_next += 1
            continue
        elif instructions[execute_next][0] == 'jmp':
            execute_next += instructions[execute_next][1]
            continue

    # print(json.dumps(instructions, indent=2))
    print(boot_counter)

    return None


exercise_input = read_input('8.2.input.test.txt')

processed_input = process_input(exercise_input)

execute_boot(processed_input)

for key, value in processed_input.items():
    if value[0] == 'jmp':

        modified_bootorder = copy.deepcopy(processed_input)
        modified_bootorder[key][0] = 'nop'

        if execute_boot(modified_bootorder) is not None:
            print(key)
            print(value)

    elif value[0] == 'nop':

        modified_bootorder = copy.deepcopy(processed_input)
        modified_bootorder[key][0] = 'jmp'

        if execute_boot(modified_bootorder) is not None:
            print(key)
            print(value)

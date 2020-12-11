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

available_options = dict()

numbers_as_list = list(numbers_as_set)

options_dictionary = dict()

def how_many_options_available(previous_adapter: int, adapters: list) -> int:
    print(f"Current dict size: {len(options_dictionary)}. Currently running with {len(adapters)} adapters.")

    if len(adapters) == 0 or adapters is None:
        return 0
    elif len(adapters) == 1:
        if adapters.pop() - previous_adapter > 3:
            return 0
        else:
            return 1
    
    empty_str = " "
    adapters_string = empty_str.join(str(elem) for elem in adapters)

    if adapters_string in options_dictionary:
        return options_dictionary[adapters_string]

    options_available = 0

    for index, adapter in enumerate(adapters):
        if adapter - previous_adapter <= 3:
            options_available += how_many_options_available(adapter, adapters[index + 1:])
            # options_available += how_many_options_available(adapter, adapters[index + 2:])
            # options_available += how_many_options_available(adapter, adapters[index + 3:])
        else:
            break
    
    if len(adapters) < 85:
        options_dictionary[adapters_string] = options_available

    return options_available


print(how_many_options_available(0, numbers_as_list))

print(options_dictionary)
#     difference = number - numbers_as_list[index-1]

#     difference_count[difference] += 1
#     # print(difference)

# print(difference_count)
# print(list(numbers_as_set))
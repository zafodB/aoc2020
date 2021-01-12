def open_file(location:str='10.1.input.test.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: dict) -> dict:
    processed_input = []
    for line in lines:
        processed_input.append(int(line.strip(), base=10))
    
    return processed_input

intpu_raw = open_file(location='10.1.input.txt')
input_ready = list(set(process_input(intpu_raw)))

# Create empty dictionary with zeros
options_dict = {}
for adapter in input_ready:
    options_dict[adapter] = 0

# Manually add the first 0 output
options_dict[0] = 1

# Manually add the highest output
highest_adapter = sorted(options_dict)[-1]
options_dict[highest_adapter+3] = 0

# Iterate over sorted dictionary items.
for adapter in sorted(options_dict):
    if adapter == 0:
        continue

    options = 0
    # Look back three adapter values. If value exists in the collection, add it's options to current options.
    for i in range(adapter-3, adapter):
        if i in options_dict:
            options += options_dict[i]
    
    options_dict[adapter] = options

    
print(options_dict[sorted(options_dict)[-1]])
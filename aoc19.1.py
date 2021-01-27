import re

letter_a_pattern = r' *"a" *'
letter_b_pattern = r' *"b" *'
number_pattern = r' *[0-9]+ *'


def open_file(location:str='19.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> list:
    rules = {}

    for line_index, line in enumerate(lines):
        if line == '\n':
            break
        
        rule_number, rule_content = line.split(':')
        rules[int(rule_number)] = rule_content.replace('\n','')

    messages = []

    for line in lines[line_index+1:]:
        messages.append(line.replace('\n', ''))
    
    return rules, messages

def assemble_rule(rule_number: int) -> str:

    rule = rules[rule_number]

    if re.fullmatch(letter_a_pattern, rule):
        # print(f'found it at index {rule_number}')
        return 'a'
    elif re.fullmatch(letter_b_pattern, rule):
        return 'b'
    elif rule.count('|') == 0:
        complete_rule = ''

        for number in re.findall(number_pattern, rule):
        
            complete_rule += assemble_rule(int(number.replace(' ', '')))
        
        return complete_rule

    elif rule.count('|') == 1:
        first_half, second_half = rule.split('|')

        first_half_complete = ''
        second_half_complete = ''

        for match in re.findall(number_pattern, first_half):
            first_half_complete += assemble_rule(int(match.replace(' ', '')))
        
        for match in re.findall(number_pattern, second_half):
            second_half_complete += assemble_rule(int(match.replace(' ', '')))
        
        return ('(' + first_half_complete + '|' + second_half_complete +')')

    else:
        raise ValueError('Got too many pipes in a rule! Best I can do is 1 pipe.')
    

# rules, messages = process_input(open_file('19.1.input.test.txt'))
rules, messages = process_input(open_file())

final_rule = assemble_rule(rule_number=0) + '$'

print(rules)
print(final_rule)

matching_messages = 0

with open('unmatched_messages.txt', 'w+', encoding='utf8') as output_file:
    for message in messages:
        if re.fullmatch(final_rule, message):
            matching_messages += 1
        else:
            output_file.write(message + '\n')

print(matching_messages)
# print(messages)
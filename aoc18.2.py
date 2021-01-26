import re

partentheses_pattern = r'(\((\+|\*| |[0-9])*\))'
addition_pattern = r'([0-9]+ *\+ *[0-9]+)'
multiplication_pattern = r'([0-9]+ *\* *[0-9]+)'

def open_file(location:str='18.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> list:
    return [line.replace('\n', '') for line in lines]


def evaluate_expression(expression: str) -> int:
    inside_partentheses = re.findall(partentheses_pattern, expression)
    
    while len(inside_partentheses) > 0:
        partial_result = evaluate_expression(inside_partentheses[0][0].replace('(', '').replace(')', ''))
        expression = expression.replace(inside_partentheses[0][0], str(partial_result), 1)

        inside_partentheses = re.findall(partentheses_pattern, expression)

    addition_matches = re.findall(addition_pattern, expression)

    while(len(addition_matches) > 0):
        addition_match = addition_matches[0]

        summands = addition_match.split('+')
        partial_result = int(summands[0].replace(' ', ''), base=10) + int(summands[1].replace(' ', ''), base=10)
        expression = expression.replace(addition_match, str(partial_result), 1)

        addition_matches = re.findall(addition_pattern, expression)
        
    multiplication_matches = re.findall(multiplication_pattern, expression)

    while(len(multiplication_matches) > 0):
        multiplication_match = multiplication_matches[0]

        multiplicands = multiplication_match.split('*')
        partial_result = int(multiplicands[0].replace(' ', ''), base=10) * int(multiplicands[1].replace(' ', ''), base=10)
        expression = expression.replace(multiplication_match, str(partial_result), 1)
        
        multiplication_matches = re.findall(multiplication_pattern, expression)

    return expression

# expressions = process_input(open_file('18.1.input.test.txt'))
expressions = process_input(open_file())

great_sum = 0
for expression in expressions:
    print(expression)
    print(int(evaluate_expression(expression)))
    # print()
    great_sum += int(evaluate_expression(expression), base=10)

print(great_sum)
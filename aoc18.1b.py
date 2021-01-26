import re

partentheses_pattern = r'(\((\+|\*| |[0-9])*\))'
addition_or_multiplication_pattern = r'([0-9]+ *(\+|\*) *[0-9]+)'


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

    operation_matches = re.findall(addition_or_multiplication_pattern, expression)

    while len(operation_matches) > 0:
        operation_match = operation_matches[0][0]

        if '+' in operation_match:
            summands = operation_match.split('+')
            partial_result = int(summands[0].replace(' ', ''), base=10) + int(summands[1].replace(' ', ''), base=10)

        elif '*' in operation_match:
            multiplicands = operation_match.split('*')
            partial_result = int(multiplicands[0].replace(' ', ''), base=10) * int(multiplicands[1].replace(' ', ''), base=10)
        
        expression = expression.replace(operation_match, str(partial_result), 1)

        operation_matches = re.findall(addition_or_multiplication_pattern, expression)

    return expression
        

# expressions = process_input(open_file('18.1.input.test.txt'))
expressions = process_input(open_file())

great_sum = 0
for expression in expressions:
    # print(expression)
    # print(int(evaluate_expression(expression)))
    # print()
    great_sum += int(evaluate_expression(expression), base=10)

print(great_sum)
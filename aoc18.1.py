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


expressions = process_input(open_file('18.1.input.test.txt'))


def evaluate_expression(expression: str) -> int:
    inside_partentheses = re.findall(partentheses_pattern, expression)
    
    for parentheses_match in inside_partentheses:
        partial_result = evaluate_expression(parentheses_match[0].replace('(', '').replace(')', ''))
        expression = expression.replace(parentheses_match[0], str(partial_result))


    addition_matches = re.findall(addition_pattern, expression)

    for addition_match in addition_matches:
        summands = addition_match.split('+')
        partial_result = int(summands[0].replace(' ', ''), base=10) + int(summands[1].replace(' ', ''), base=10)
        expression = expression.replace(addition_match, str(partial_result))

    multiplication_matches = re.findall(multiplication_pattern, expression)

    # Good solution if addition ALWAYS preceeds multiplication
    while(len(multiplication_matches) > 0):
        for multiplication_match in multiplication_matches:
            multiplicands = multiplication_match.split('*')
            partial_result = int(multiplicands[0].replace(' ', ''), base=10) * int(multiplicands[1].replace(' ', ''), base=10)
            expression = expression.replace(multiplication_match, str(partial_result))
        
        multiplication_matches = re.findall(multiplication_pattern, expression)

    return expression
        


for expression in expressions:
    print(expression)
    print(evaluate_expression(expression))

# print(expressions)
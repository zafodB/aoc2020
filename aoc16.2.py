import re

def open_file(location:str='16.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> (list, list, list):
    input_part = 'rules'

    rules = []
    rule_pattern = r'[0-9]*-[0-9]*'

    my_ticket = None
    other_tickets = []

    for line in lines:
        if input_part == 'rules':
            if line == '\n':
                input_part = 'my-ticket'
                continue
            
            rule = []
            ranges = re.findall(rule_pattern, line)
            for range in ranges:
                bounds = range.split('-')
                rule.append((int(bounds[0], base=10), int(bounds[1], base=10)))

            rule_name = line.split(':')[0]

            rules.append((rule_name, rule))
    
        elif input_part == 'my-ticket':
            if line == '\n':
                input_part = 'other-tickets'
                continue
            elif line == 'your ticket:\n':
                continue
            
            numbers = line.replace('\n', '').split(',')
            my_ticket = [int(_, base=10) for _ in numbers]

        elif input_part == 'other-tickets':
            if line == 'nearby tickets:\n':
                continue
            ticket = []
            for number in line.replace('\n', '').split(','):
                ticket.append(int(number, base=10))
            other_tickets.append(ticket)
    
    return (rules, my_ticket, other_tickets)

ticket_rules, my_ticket, other_tickets = process_input(open_file())
# ticket_rules, my_ticket, other_tickets = process_input(open_file('16.1.input.test.txt'))

rule_names = []
for rule in ticket_rules:
    rule_names.append(rule[0])

print(my_ticket)

# Determine valid tickets
valid_tickets = []
for ticket in other_tickets:
    ticket_valid = True

    for number in ticket:
        rule_met = False

        for rule in ticket_rules:
            if (number >= rule[1][0][0] and number <= rule[1][0][1]) or (number >= rule[1][1][0] and number <= rule[1][1][1]):
                
                rule_met = True
                break
            else:
                continue
        
        if not rule_met:
            ticket_valid = False
            break
        
    if ticket_valid:
        valid_tickets.append(ticket)

possible_fields = []

for i in range(len(valid_tickets[0])):
    possible_fields.append(rule_names.copy())

# Determine fields
for ticket in valid_tickets:
    for index, number in enumerate(ticket):
        for rule in ticket_rules:
            if (number >= rule[1][0][0] and number <= rule[1][0][1]) or (number >= rule[1][1][0] and number <= rule[1][1][1]):
                continue
            else:
                if rule[0] in possible_fields[index]:
                    possible_fields[index].remove(rule[0])


change = True
while change:
    change = False
    for index, field in enumerate(possible_fields):
        if len(field) == 1:
            only_remaining_rule = possible_fields[index][0]

            for field_index, field in enumerate(possible_fields):
                if field_index != index:
                    if only_remaining_rule in field:
                        possible_fields[field_index].remove(only_remaining_rule)
                        change = True


fields_of_interes = []

for index, field in enumerate(possible_fields):
    if field[0][:4] == 'depa':
        fields_of_interes.append(index)

result = 1

for field in fields_of_interes:
    result *= my_ticket[field]

print(result)



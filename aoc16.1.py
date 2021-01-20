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

            rules.append(rule)
    
        elif input_part == 'my-ticket':
            if line == '\n':
                input_part = 'other-tickets'
                continue
            
            my_ticket = line
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

print(ticket_rules)

ticket_scanning_error_rate = 0

for ticket in other_tickets:
    for number in ticket:
        rule_met = False

        for rule in ticket_rules:
            if (number >= rule[0][0] and number <= rule[0][1]) or (number >= rule[1][0] and number <= rule[1][1]):
                
                rule_met = True
                break
            else:
                continue
        
        if not rule_met:
            ticket_scanning_error_rate += number
            break

print(ticket_scanning_error_rate)



import re

letter_a_pattern = r' *"a" *'
letter_b_pattern = r' *"b" *'
number_pattern = r' *[0-9]+ *'


def open_file(location:str='19.2.input.txt') -> list:
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
# rules, messages = process_input(open_file())
# rules, messages = process_input(open_file('19.2.input.2.txt'))
rules, messages = process_input(open_file('19.1.input.txt'))

final_rule = assemble_rule(rule_number=0) + '$'

# final_rule_adjusted_8 = '(((b((a(a|b)(a(a|b)|bb)|b(a(ba|ab)|bab))b|((aaa|b(b(a|b)|ab))a|(bba|a(aa|ab))b)a)|a(a(b((ba|a(a|b))a|(ba|bb)b)|a(b(a|b)(a|b)|aba))|b(b(a(ba|bb)|b(a|b)(a|b))|a(aab|b(aa|ab)))))b|(b(a((aba|abb)b|(aaa|abb)a)|b(((a(a|b)|bb)b|(ba|bb)a)b|(a(aa|b(a|b))|bab)a))|a((b(aba|aab)|a(bba|bab))a|(b(a(ba|bb)|b(ba|a(a|b)))|a(b(a(a|b)|bb)|a(a|b)(a|b)))b))a)a|((a((b(b(ba|a(a|b))|aab)|a((a(a|b)|bb)a|aab))a|((a(aa|ab)|b(ba|a(a|b)))a|(baa|abb)b)b)|b((a(b(aa|b(a|b))|aba)|b(bbb|a(ba|ab)))a|(b(b(aa|b(a|b))|aba)|a(aab|bab))b))a|(b(a(b(b(ba|ab)|a(aa|b(a|b)))|a(aba|aab))|b(b(b(ba|ab)|a(aa|b(a|b)))|a(a|b)(aa|b(a|b))))|a(a(b(b(a(a|b)|bb)|aaa)|a(a(a(a|b)|bb)|b(ba|bb)))|b((a(ba|a(a|b))|bab)b|((aa|b(a|b))b|(ba|ab)a)a)))b)b)+(((b((a(a|b)(a(a|b)|bb)|b(a(ba|ab)|bab))b|((aaa|b(b(a|b)|ab))a|(bba|a(aa|ab))b)a)|a(a(b((ba|a(a|b))a|(ba|bb)b)|a(b(a|b)(a|b)|aba))|b(b(a(ba|bb)|b(a|b)(a|b))|a(aab|b(aa|ab)))))b|(b(a((aba|abb)b|(aaa|abb)a)|b(((a(a|b)|bb)b|(ba|bb)a)b|(a(aa|b(a|b))|bab)a))|a((b(aba|aab)|a(bba|bab))a|(b(a(ba|bb)|b(ba|a(a|b)))|a(b(a(a|b)|bb)|a(a|b)(a|b)))b))a)a|((a((b(b(ba|a(a|b))|aab)|a((a(a|b)|bb)a|aab))a|((a(aa|ab)|b(ba|a(a|b)))a|(baa|abb)b)b)|b((a(b(aa|b(a|b))|aba)|b(bbb|a(ba|ab)))a|(b(b(aa|b(a|b))|aba)|a(aab|bab))b))a|(b(a(b(b(ba|ab)|a(aa|b(a|b)))|a(aba|aab))|b(b(b(ba|ab)|a(aa|b(a|b)))|a(a|b)(aa|b(a|b))))|a(a(b(b(a(a|b)|bb)|aaa)|a(a(a(a|b)|bb)|b(ba|bb)))|b((a(ba|a(a|b))|bab)b|((aa|b(a|b))b|(ba|ab)a)a)))b)b)((a((a((abb|b(a(a|b)|bb))a|((ba|bb)a|(ba|a(a|b))b)b)|b(a(bbb|(aa|b(a|b))a)|b(b(b(a|b)|ab)|abb)))a|(b((a(bb|aa)|bba)a|((ab|bb)b|(ba|bb)a)b)|a(a(b(aa|ab)|aba)|b(bba|a(b(a|b)|ab))))b)|b((((bbb|(aa|b(a|b))a)a|(b(ba|ab)|a(ba|a(a|b)))b)a|(a(a|b)(aa|b(a|b))|b(aaa|(ba|a(a|b))b))b)a|(((a(ba|ab)|b(ba|a(a|b)))a|((a(a|b)|bb)b|aaa)b)b|(aabb|((a(a|b)|bb)b|aaa)a)a)b))b|((b(b(((aa|b(a|b))a|(ab|bb)b)b|((a(a|b)|bb)b|aaa)a)|a((b(a|b)(a|b)|aba)a|(aba|bba)b))|a(a((a|b)(aa|ab)b|(bbb|aaa)a)|b((baa|a(a(a|b)|bb))a|((aa|ab)b|baa)b)))b|((a((baa|abb)a|(baa|bbb)b)|b(a(b(a|b)(a|b)|a(aa|ab))|b(bab|(aa|ab)a)))b|(b(a(b(a|b)(a|b)|a(ba|ab))|b(b(aa|b(a|b))|aab))|a((b(b(a|b)|ab)|a(a(a|b)|bb))b|(b(aa|b(a|b))|a(ba|a(a|b)))a))a)a)a)$'

# Must replace x with 1, 2, ..
final_rule_adjusted_8_42 = '(((b((a(a|b)(a(a|b)|bb)|b(a(ba|ab)|bab))b|((aaa|b(b(a|b)|ab))a|(bba|a(aa|ab))b)a)|a(a(b((ba|a(a|b))a|(ba|bb)b)|a(b(a|b)(a|b)|aba))|b(b(a(ba|bb)|b(a|b)(a|b))|a(aab|b(aa|ab)))))b|(b(a((aba|abb)b|(aaa|abb)a)|b(((a(a|b)|bb)b|(ba|bb)a)b|(a(aa|b(a|b))|bab)a))|a((b(aba|aab)|a(bba|bab))a|(b(a(ba|bb)|b(ba|a(a|b)))|a(b(a(a|b)|bb)|a(a|b)(a|b)))b))a)a|((a((b(b(ba|a(a|b))|aab)|a((a(a|b)|bb)a|aab))a|((a(aa|ab)|b(ba|a(a|b)))a|(baa|abb)b)b)|b((a(b(aa|b(a|b))|aba)|b(bbb|a(ba|ab)))a|(b(b(aa|b(a|b))|aba)|a(aab|bab))b))a|(b(a(b(b(ba|ab)|a(aa|b(a|b)))|a(aba|aab))|b(b(b(ba|ab)|a(aa|b(a|b)))|a(a|b)(aa|b(a|b))))|a(a(b(b(a(a|b)|bb)|aaa)|a(a(a(a|b)|bb)|b(ba|bb)))|b((a(ba|a(a|b))|bab)b|((aa|b(a|b))b|(ba|ab)a)a)))b)b)+(((b((a(a|b)(a(a|b)|bb)|b(a(ba|ab)|bab))b|((aaa|b(b(a|b)|ab))a|(bba|a(aa|ab))b)a)|a(a(b((ba|a(a|b))a|(ba|bb)b)|a(b(a|b)(a|b)|aba))|b(b(a(ba|bb)|b(a|b)(a|b))|a(aab|b(aa|ab)))))b|(b(a((aba|abb)b|(aaa|abb)a)|b(((a(a|b)|bb)b|(ba|bb)a)b|(a(aa|b(a|b))|bab)a))|a((b(aba|aab)|a(bba|bab))a|(b(a(ba|bb)|b(ba|a(a|b)))|a(b(a(a|b)|bb)|a(a|b)(a|b)))b))a)a|((a((b(b(ba|a(a|b))|aab)|a((a(a|b)|bb)a|aab))a|((a(aa|ab)|b(ba|a(a|b)))a|(baa|abb)b)b)|b((a(b(aa|b(a|b))|aba)|b(bbb|a(ba|ab)))a|(b(b(aa|b(a|b))|aba)|a(aab|bab))b))a|(b(a(b(b(ba|ab)|a(aa|b(a|b)))|a(aba|aab))|b(b(b(ba|ab)|a(aa|b(a|b)))|a(a|b)(aa|b(a|b))))|a(a(b(b(a(a|b)|bb)|aaa)|a(a(a(a|b)|bb)|b(ba|bb)))|b((a(ba|a(a|b))|bab)b|((aa|b(a|b))b|(ba|ab)a)a)))b)b){x}((a((a((abb|b(a(a|b)|bb))a|((ba|bb)a|(ba|a(a|b))b)b)|b(a(bbb|(aa|b(a|b))a)|b(b(b(a|b)|ab)|abb)))a|(b((a(bb|aa)|bba)a|((ab|bb)b|(ba|bb)a)b)|a(a(b(aa|ab)|aba)|b(bba|a(b(a|b)|ab))))b)|b((((bbb|(aa|b(a|b))a)a|(b(ba|ab)|a(ba|a(a|b)))b)a|(a(a|b)(aa|b(a|b))|b(aaa|(ba|a(a|b))b))b)a|(((a(ba|ab)|b(ba|a(a|b)))a|((a(a|b)|bb)b|aaa)b)b|(aabb|((a(a|b)|bb)b|aaa)a)a)b))b|((b(b(((aa|b(a|b))a|(ab|bb)b)b|((a(a|b)|bb)b|aaa)a)|a((b(a|b)(a|b)|aba)a|(aba|bba)b))|a(a((a|b)(aa|ab)b|(bbb|aaa)a)|b((baa|a(a(a|b)|bb))a|((aa|ab)b|baa)b)))b|((a((baa|abb)a|(baa|bbb)b)|b(a(b(a|b)(a|b)|a(aa|ab))|b(bab|(aa|ab)a)))b|(b(a(b(a|b)(a|b)|a(ba|ab))|b(b(aa|b(a|b))|aab))|a((b(b(a|b)|ab)|a(a(a|b)|bb))b|(b(aa|b(a|b))|a(ba|a(a|b)))a))a)a)a){x}$'
print(assemble_rule(31))
print()
# print(rules)
print(final_rule)

matching_messages = 0

# with open('unmatched_messages2.txt', 'w+', encoding='utf8') as output_file:
for message in messages:
    if re.fullmatch(final_rule_adjusted_8_42, message):
        matching_messages += 1
    else:
        pass
            # output_file.write(message + '\n')

print(matching_messages)
# print(messages)
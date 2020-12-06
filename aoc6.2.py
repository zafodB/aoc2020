with open('6.1.input.txt', 'r', encoding='utf8') as input_file:
    input_lines = input_file.readlines()

questions_sum = 0

group = set()
new_group = True

for line in input_lines:
    if line == "\n":
        this_group_questions = len(group)
        questions_sum += this_group_questions

        new_group = True
        continue
    
    if new_group:
        group = set(list(line.strip()))
        new_group = False
    else:
        group = group.intersection(set(list(line.strip())))
  
print(questions_sum)
    
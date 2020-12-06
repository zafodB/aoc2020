with open('6.1.input.txt', 'r', encoding='utf8') as input_file:
    input_lines = input_file.readlines()

questions_sum = 0

group = set()

for line in input_lines:
    if line == "\n":
        # print(group)
        this_group_questions = len(group)
        questions_sum += this_group_questions

        group = set()
        continue
    
    group.update(list(line.strip()))
  
print(questions_sum)
    
print("hello there")

with open('3.1.input.txt', 'r', encoding='utf8') as inputfile:
    lines = inputfile.readlines()

print(lines[0])

position = 0
linelenght = len(lines[0]) - 1
trees = 0

for index, line in enumerate(lines):
    if index % 2 == 1:
        continue

    # print(index)
    line = list(line)[:-1]

    if line[position % linelenght] == '#':
        trees += 1
    
    
    # print(line)
    line[position % linelenght] = "X"
    line = "".join([str(element) for element in line])

    position+=1

    print(line)

print(trees)

'''

Right 1, down 1. 84
Right 3, down 1. 198
Right 5, down 1. 72
Right 7, down 1. 81
Right 1, down 2. 53
'''
import re

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def byr_check(input: str) -> bool:
    try:
        if len(input) != 4:
            return False

        year = int(input, base=10)

        return year >= 1920 and year <= 2002
           
    except:
        return False


def iyr_check(input: str) -> bool:
    try:
        if len(input) != 4:
            return False

        year = int(input, base=10)

        return year >= 2010 and year <= 2020

    except:
        return False


def eyr_check(input: str) -> bool:
    try:
        if len(input) != 4:
            return False

        year = int(input, base=10)
        return year >= 2020 and year <= 2030
           
    except:
        return False


def hgt_check(input: str) -> bool:
    try:

        height = int(input[:-2], base=10)
        if input[-2:] == "cm" and height >= 150 and height <= 193:
            return True

        elif input[-2:] == "in" and height >= 59 and height <= 76:
            return True
        else:
            return False

    except:
        return False


def hcl_check(input: str) -> bool:
    try:
        pattern = re.compile('#([0-9]|[a-f]){6}')

        return pattern.fullmatch(input) is not None
            
    except:
        return False


def ecl_check(input: str) -> bool:
    return input in eye_colors


def pid_check(input: str) -> bool:
    try:
        pattern = re.compile('[0-9]{9}')

        return pattern.fullmatch(input) is not None
    except:
        return False


features = {
    'byr': [0, byr_check],
    'iyr': [1, iyr_check],
    'eyr': [2, eyr_check],
    'hgt': [3, hgt_check],
    'hcl': [4, hcl_check],
    'ecl': [5, ecl_check],
    'pid': [6, pid_check]
    # 'cid': 7

}

def check_input():

    with open('4.1input.txt', 'r', encoding='utf8') as inputfile:
        input_text = inputfile.readlines()

    valid_passports = 0
    passport_features = [False for _ in range(7)]

    for line in input_text:
        if line == "\n":
            if all(passport_features):
                valid_passports += 1

            passport_features = [False for _ in range(7)]
            continue

        items = line.split(" ")
        for item in items:

            if item[:3] in features:

                print("now checking: " + str(features[item[:3]][1].__name__) + " with input: " + item[4:].strip())
                print(features[item[:3]][1](item[4:].strip()))

                passport_features[features[item[:3]][0]] = features[item[:3]][1](item[4:].strip())

    print(valid_passports)


check_input()
# print(pid_check("190cm"))
# print(pid_check("190in"))
# print(pid_check("#123ab0"))
# print(pid_check("0000000000"))
# print(pid_check(None))

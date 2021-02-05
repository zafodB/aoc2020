def open_file(location:str='21.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> dict:
    all_foods = []
    all_alergens = set()
    all_ingredients = set()

    for line in lines:
        ingredients_raw, alergens_raw = line.split(' (')
        ingredients = set(ingredients_raw.split(' '))
        alergens = [alergen.replace(' ', '').replace(')', '') for alergen in alergens_raw.replace('contains', '').replace('\n', '').split(', ')]
        all_alergens.update(alergens)
        all_ingredients.update(ingredients)

        all_foods.append((ingredients, alergens))

    return all_foods, all_alergens, all_ingredients


all_foods_input, alergens, ingredients = process_input(open_file())
# all_foods_input, alergens, ingredients = process_input(open_file('21.1.input.test.txt'))

non_cause_ingredients = {}

for alergen in alergens:
    non_cause_ingredients[alergen] = set()

for food in all_foods_input:
    for food_alergen in food[1]:
        non_cause_ingredients[food_alergen].update(ingredients.difference(food[0]))

harmless_ingredients = set.intersection(*list(non_cause_ingredients.values()))

harmless_count = 0
for food in all_foods_input:
    harmless_count += len(harmless_ingredients.intersection(food[0]))

print(harmless_count)

# print(len(set.intersection(*list(non_cause_ingredients.values()))))
# print(non_cause_ingredients)

# print(f'List of alergens: {alergens}')
# print(f'List of ingredients: {ingredients}')

# print(all_foods_input)
import networkx as nx
import matplotlib.pyplot as plt
import json

def read_file(file_location: str = '7.1input.test.txt') -> list:
    with open(file_location, 'r', encoding='utf8') as input_file:
        input_lines = input_file.readlines()

    return input_lines

def map_bags_to_rules(input_lines: list) -> dict:
    bag_rules = {}

    for line in input_lines:
        words = line.split()
        
        larger_bag = words[0] + words[1]

        smaller_bags = {}

        for index, word in enumerate(words):
            if index < 4:
                continue
            if index == 4 and word == 'no':
                break

            if index % 4 == 0:
                quantity = word
            elif index % 4 == 2:
                smaller_bag = words[index-1] + word
                smaller_bags[smaller_bag] = quantity
        
        bag_rules[larger_bag] = smaller_bags
            

    # print(json.dumps(bag_rules, indent=2))
    return bag_rules

def make_graph(rules_input: dict):
    bag_graph = nx.DiGraph()
    
    for big_bag in rules_input.keys():
        bag_graph.add_node(big_bag)

    for big_bag in rules_input.keys():
        for small_bag in rules_input[big_bag].keys():
            bag_graph.add_edge(big_bag, small_bag, weight=rules_input[big_bag][small_bag])    

    return bag_graph

lines = read_file('7.1.input.txt')
rules = map_bags_to_rules(lines)
mygraph = make_graph(rules)

# my_graph = nx.DiGraph()

# my_graph.add_node('blue')
# my_graph.add_node('gold')
# my_graph.add_edge('blue', 'gold', weight=3)

predecessor_set_complete = set()
predecessor_set_checkout = {'shinygold'}

while len(predecessor_set_checkout) > 0:
    checkout = predecessor_set_checkout.pop()

    for predecessor in mygraph.predecessors(checkout):
        predecessor_set_complete.add(predecessor)
        predecessor_set_checkout.add(predecessor)
        # print(predecessor)

# nx.draw_networkx(mygraph)

# plt.show()
print(predecessor_set_complete)
print(len(predecessor_set_complete))
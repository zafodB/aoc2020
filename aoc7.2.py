import networkx as nx
import matplotlib.pyplot as plt
import json

"""
Read input from file
"""
def read_file(file_location: str = '7.1input.test.txt') -> list:
    with open(file_location, 'r', encoding='utf8') as input_file:
        input_lines = input_file.readlines()

    return input_lines

"""
Process input by splitting lines into words and figuring which words are colours and which are quanitites (based on position of the word in the sentence).
Return as a dictionary with form {bag a: contains x of bag b}
"""
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
            
    return bag_rules

"""
Turn bag rules into a directed graph where directed edge from a to b indicates that a must contain b and edge weight is the number of required bags.
"""
def make_graph(rules_input: dict):
    bag_graph = nx.DiGraph()
    
    for big_bag in rules_input.keys():
        bag_graph.add_node(big_bag)

    for big_bag in rules_input.keys():
        for small_bag in rules_input[big_bag].keys():
            bag_graph.add_edge(big_bag, small_bag, weight=rules_input[big_bag][small_bag])    

    return bag_graph

"""
Recursive function to find the number of bags within the given bag. If a bag has no further bags in it, return 1. Otherwise,
determine how many bags are in it.
"""
def find_bags_within(work_on_node) -> int:
    if not any(mygraph.successors(work_on_node)):
        return 1
    
    # Initiate as 1 since we need to count the parent bag as well.
    total_sum = 1

    for successor in mygraph.successors(work_on_node):
        weight = int(mygraph.get_edge_data(work_on_node, successor)['weight'], base=10)
        
        total_sum += weight * find_bags_within(successor)
    
    return total_sum


lines = read_file('7.1.input.txt')
rules = map_bags_to_rules(lines)
mygraph = make_graph(rules)

# Gotta remember to substract 1, because we are not supposed to include the outermost bag in the count.
print(find_bags_within('shinygold') - 1)

# nx.draw(mygraph.subgraph('shinygold'))
# plt.show()



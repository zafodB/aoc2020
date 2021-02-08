from tqdm import tqdm
import networkx as nx

puzzle_input = '463528179' 
# puzzle_input = '389125467' # test input

number_of_cups = 1000000
# number_of_cups = 9

cup_graph = nx.DiGraph()

# previous = int(puzzle_input[-1])
previous = 1000000

for cup in puzzle_input:
    current = int(cup)
    cup_graph.add_edge(previous, current)
    previous = current

for more_cup in range(10, number_of_cups + 1):
    cup_graph.add_edge(previous, more_cup)
    previous = more_cup


def make_move(input_graph: nx.DiGraph, current_cup: int):
    start_pickup = next(input_graph.successors(current_cup))

    input_graph.remove_edge(current_cup, start_pickup)

    pick_three = [start_pickup]

    latest_end = start_pickup
    for i in range(2):
        
        latest_end = next(input_graph.successors(latest_end))
        pick_three.append(latest_end)

    next_after_pickup = next(input_graph.successors(latest_end))

    input_graph.remove_edge(latest_end, next_after_pickup)
    input_graph.add_edge(current_cup, next_after_pickup)

    destination_cup = current_cup - 1
    if destination_cup < 1:
        destination_cup += number_of_cups

    while destination_cup in pick_three:
        destination_cup -= 1

        # wrap around
        if destination_cup < 1:
            destination_cup += number_of_cups

    destination_end = next(input_graph.successors(destination_cup))

    input_graph.remove_edge(destination_cup, destination_end)

    input_graph.add_edge(destination_cup, start_pickup)
    input_graph.add_edge(latest_end, destination_end)
    
    return input_graph


current_cup = int(puzzle_input[0])
for number_of_moves in tqdm(range(10000000)):
    cup_graph = make_move(cup_graph, current_cup)

    current_cup = next(cup_graph.successors(current_cup))

print(next(cup_graph.successors(1)))
print(next(cup_graph.successors(next(cup_graph.successors(1)))))

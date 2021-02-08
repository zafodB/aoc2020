from queue import Queue

def open_file(location:str='22.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> dict:
    player1_deck = Queue()
    player2_deck = Queue()

    now_processing_player1 = True
    for line in lines:
        if line[:-1] == 'Player 1:' or line == '\n':
            continue
        elif line[:-1] == 'Player 2:':
            now_processing_player1 = False
        else:
            card = line.replace('\n', '')

            if now_processing_player1:
                player1_deck.put(int(card))
            else:
                player2_deck.put(int(card))

    return player1_deck, player2_deck


player1_deck, player2_deck = process_input(open_file())
# player1_deck, player2_deck = process_input(open_file('22.1.input.test.txt'))

while not player1_deck.empty() and not player2_deck.empty():
    player1_hand, player2_hand = player1_deck.get(), player2_deck.get()

    if player1_hand > player2_hand:
        player1_deck.put(player1_hand)
        player1_deck.put(player2_hand)
    else:
        player2_deck.put(player2_hand)
        player2_deck.put(player1_hand)

print(list(player1_deck.queue))
print(list(player2_deck.queue))

if player1_deck.empty:
    winner_deck = player2_deck
else:
    winner_deck = player1_deck

end_score = 0
for index, item in enumerate(reversed(list(winner_deck.queue))):
    end_score += (item * (index+1))

print(end_score)
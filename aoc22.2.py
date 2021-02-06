from collections import deque

P1_WINS = '12'
P2_WINS = '34'


def open_file(location:str='22.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


def process_input(lines: list) -> dict:
    player1_deck = deque()
    player2_deck = deque()

    now_processing_player1 = True
    for line in lines:
        if line[:-1] == 'Player 1:' or line == '\n':
            continue
        elif line[:-1] == 'Player 2:':
            now_processing_player1 = False
        else:
            card = line.replace('\n', '')

            if now_processing_player1:
                player1_deck.append(int(card))
            else:
                player2_deck.append(int(card))

    return player1_deck, player2_deck


def play_round(p1_deck: deque, p2_deck: deque):
    p1_hand = p1_deck.popleft()
    p2_hand = p2_deck.popleft()

    if len(p1_deck) < p1_hand or len(p2_deck) < p2_hand:
        if p1_hand > p2_hand:
            return P1_WINS, (p1_hand, p2_hand)
        else:
            return P2_WINS, (p2_hand, p1_hand)
    else:
        next_round_p1 = deque(list(p1_deck)[:p1_hand])
        next_round_p2 = deque(list(p2_deck)[:p2_hand])

        winner = play_game(next_round_p1, next_round_p2)[0]

        if winner == P1_WINS:
            return P1_WINS, (p1_hand, p2_hand)
        else:
            return P2_WINS, (p2_hand, p1_hand)


def play_game(player1_deck, player2_deck):

    p1_deck_history = set()
    p2_deck_history = set()

    while len(player1_deck) != 0 and len(player2_deck) != 0:

        if tuple(player1_deck) in p1_deck_history or tuple(player2_deck) in p2_deck_history:
            return P1_WINS, player1_deck, player2_deck

        p1_deck_history.add(tuple(player1_deck))
        p2_deck_history.add(tuple(player2_deck))

        winner, new_cards = play_round(player1_deck, player2_deck)
        if winner == P1_WINS:
            player1_deck.append(new_cards[0])
            player1_deck.append(new_cards[1])
        else:
            player2_deck.append(new_cards[0])
            player2_deck.append(new_cards[1])

    
    if len(player1_deck) == 0:
        game_winner = P2_WINS
    else:
        game_winner = P1_WINS

    return game_winner, player1_deck, player2_deck


player1_deck, player2_deck = process_input(open_file())
# player1_deck, player2_deck = process_input(open_file('22.1.input.test.txt'))
# player1_deck, player2_deck = process_input(open_file('22.2.input.test.txt'))

play_game(player1_deck, player2_deck)

print(list(player1_deck))
print(list(player2_deck))

if len(player1_deck) == 0:
    winner_deck = player2_deck
else:
    winner_deck = player1_deck

end_score = 0
for index, item in enumerate(reversed(list(winner_deck))):
    end_score += (item * (index+1))

print(end_score)
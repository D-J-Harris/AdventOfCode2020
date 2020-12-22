"""Crab Combat"""
from collections import deque


def game(player_1, player_2, first):

    prev_states = [(player_1.copy(), player_2.copy())]

    while player_1 and player_2:
        top_1 = player_1.popleft()
        top_2 = player_2.popleft()
        if not first and top_1 <= len(player_1) and top_2 <= len(player_2):
            new_player_1 = deque(list(player_1)[:top_1].copy())
            new_player_2 = deque(list(player_2)[:top_2].copy())
            winner, _ = game(new_player_1, new_player_2, False)
            if winner == 1:
                player_1.append(top_1)
                player_1.append(top_2)
            else:
                player_2.append(top_2)
                player_2.append(top_1)
        else:
            if top_1 > top_2:
                player_1.append(top_1)
                player_1.append(top_2)
            else:
                player_2.append(top_2)
                player_2.append(top_1)
        if not first:
            if (player_1, player_2) in prev_states:
                return (1, player_1)
            else:
                prev_states.append((player_1.copy(), player_2.copy()))
    return (1, player_1) if player_1 else (2, player_2)


with open('../inputs/day22.txt', 'r') as f:
    player_1 = deque()
    player_2 = deque()
    for player, block in enumerate(f.read().split('\n\n')):
        lines = block.split('\n')
        for x in lines[1:]:
            if player == 0:
                player_1.append(int(x))
            else:
                player_2.append(int(x))

ans = 0
_, end_deck = game(player_1.copy(), player_2.copy(), False)
for idx, value in enumerate(reversed(end_deck)):
    ans += (idx+1) * value

# switch third argument of game to True for puzzle 1
print(f'answer to puzzle 2 is {ans}')

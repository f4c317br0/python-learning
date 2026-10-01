import random
from collections import defaultdict
from itertools import combinations

names = input().split()
pairs = list(combinations(names, 2))
winners = defaultdict(int)
with open('tournament.txt', 'w', encoding='utf-8') as f:
    for tour in pairs:
        winner = random.choice(tour)
        winners[winner] += 1
        f.write(f'{tour[0]} vs {tour[1]}: победил {winner}.\n')
    for name in names:
        if name == names[-1]:
            f.write(f'{name} - {winners[name]}')
            break
        if winners[name] != 0:
            f.write(f'{name} - {winners[name]}\n')

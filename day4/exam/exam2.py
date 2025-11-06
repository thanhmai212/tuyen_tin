s = [int(input()) for _ in range(8)]

matches = [(0,1), (2,3), (4,5), (6,7)]

winners = []
losers = []

for a, b in matches:
    if s[a] > s[b]:
        winners.append(a)
        losers.append(b)
    elif s[a] < s[b]:
        winners.append(b)
        losers.append(a)
    else:
        winners.append(min(a, b))
        losers.append(max(a, b))

best_winner = max(winners, key=lambda i: (s[i], -i))
best_loser = max(losers, key=lambda i: (s[i], -i))

print(f"S{best_winner + 1}")
print(f"S{best_loser + 1}")
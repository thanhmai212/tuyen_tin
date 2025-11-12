n = int(input())
draws = list(map(int, input().split(" ")))

total = 0
list_k = []

for draw in draws:
    for d in draws:
        if draw < d:
            total += d - draw
        else:
            total += draw - d
    list_k.append(total)
print(min(list_k))
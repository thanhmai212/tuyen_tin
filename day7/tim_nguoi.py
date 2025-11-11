n = int(input())
cards = list(map(int, input().split()))
k = int(input())
original = cards.copy()
a = []
person = 0
for i in range(n - 1):
    x = cards.pop(0)
    y = cards.pop(0)
    if x > y:
        a.append(x)
        cards.insert(0, y)
        if x == cards[k - 1]:
            person = i + 1
            break
    else:
        a.append(y)
        cards.insert(0, x)
        if y == cards[k - 1]:
            person = i + 1
            break
a.append(cards[0])
print(person)

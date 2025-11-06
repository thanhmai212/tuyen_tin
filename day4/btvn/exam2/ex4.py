import math

n = int(input())
nums_f1_groups = list(map(int, input().split()))
c1 = c2 = c3 = c4 = 0
rooms = 0
for i in nums_f1_groups:
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1
    elif i == 3:
        c3 += 1
    elif i == 4:
        c4 += 1
rooms += c4
pair_31 = min(c3, c1)
rooms += pair_31
c3 -= pair_31
c1 -= pair_31
rooms += c3

rooms += c2 // 2
c2 %= 2

if c2 == 1:
    rooms += 1
    c1 -= min(2, c1)
if c1 > 0:
    rooms += math.ceil(c1 / 4)

print(rooms)

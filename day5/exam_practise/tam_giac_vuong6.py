import math
ab, ah = map(int, input().split(" "))

bh = ab**2 - ah**2
print(f'{math.sqrt(bh):.2f}', end=" ")
print(f'{ah**2/bh:.2f}')
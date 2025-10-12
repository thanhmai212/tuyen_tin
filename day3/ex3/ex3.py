from collections import defaultdict
from math import gcd
rectangles = defaultdict(int)
with open('RECT.INP', 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        a, b = map(int, f.readline().split(" "))
        if a > b:
            a, b = b, a
        g = gcd(a, b)
        numberator = a / g
        denominator = b / g
        signature = (numberator, denominator)
        rectangles[signature] += 1
        nums_group = len(rectangles)
        max_size_in_group = max(rectangles.values() if nums_group else 0)

with open('RECT.OUT', 'w') as f:
    f.write(f"{str(nums_group)} {str(max_size_in_group)}")
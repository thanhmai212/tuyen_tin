import math

def is_pitago(a, b, c):
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    return False

a, b, c = map(int, input().split(" "))

print(max(a, b, c))
print(math.gcd(a, b, c))
print("YES" if is_pitago(a, b, c) else "NO")
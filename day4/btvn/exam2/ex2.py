import math


def is_pefect_quare(n):
    if n < 0:
        return False
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n:
        return True


def is_step(n):
    s = str(n)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))


a, b = map(int, input().split(" "))

gcd_a_b = math.gcd(a, b)

print(gcd_a_b)
print(str(a // gcd_a_b) + '/' + str(b // gcd_a_b))

pefect_squares = []
for n in range(a, b + 1):
    if is_pefect_quare(n):
        pefect_squares.append(n)

print(*pefect_squares)
print(sum(1 for _ in range(a, b + 1) if is_step(_)))

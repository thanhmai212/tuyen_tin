from fractions import Fraction
m, n = map(int, input().split(" "))
print(sum(int(_) for _ in range(m, n + 1) if _ % 2 != 0))
print(Fraction(m, n))

found = False
for x in range(1, m // 2 + 1):
    y = m - x
    if x * y == n:
        print(x, y)
        found = True
        break
if not found:
    print("KHONG")

n, k = map(int, input().strip().split())


def is_prime(x):
    if x < 2:
        return False
    import math
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


digits = [int(d) for d in str(n)]
print(len(digits))
if k >= len(digits):
    digits = []
else:
    digits = digits[:-k]
print(0 if not digits else ''.join(map(str, digits)))
prime = 0
for d in digits[:]:
    if not is_prime(d):
        prime = d
        digits.remove(d)
        break
print(prime)

n = int(input())
total = 0
if n == 1:
    total = 10000
elif n <= 10:
    total = 10000 + (n - 1) * 9000
else:
    total = 10000 + 9 * 9000 + (n - 10) * 8000
if n > 50:
    total *= 0.9
print(int(total))

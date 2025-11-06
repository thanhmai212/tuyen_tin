import math

n = int(input())
results = []
i = int(n**0.5)
while i > 0 and n > 0:
    if i*i <= n:
        results.append(i)
        n -= i*i
    else:
        i -= 1
print(*results)
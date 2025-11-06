n = int(input())
S = 0.0
k = 0
total_T = 0

for i in range(2, n + 2):
    if i % 2 == 0:
        S += 1.0 / i
    else:
        S -= 1.0 / i

while total_T <= n * n:
    k += 1
    total_T += k * (k + 1)

print(f"{sum(int(_) for _ in str(abs(n)))}")
print(f"{S:.2f}")
print(f"{k - 1}")
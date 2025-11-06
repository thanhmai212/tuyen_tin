n = int(input())
total_s = 0

for num in range(1, n + 1):
    total_s += num / (num + 1)
print(f"{total_s:.4f}")

x = 1
while (x * (x + 1)) // 2 <= n:
    x += 1
print(x - 1)
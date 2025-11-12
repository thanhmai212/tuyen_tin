with open('DRAW.INP', 'r') as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split(" ")))

a.sort()
median = a[n // 2]
ans = 0
for i in a:
    ans += abs(i - median)
with open('DRAW.OUT', 'w') as f:
    f.write(str(ans))
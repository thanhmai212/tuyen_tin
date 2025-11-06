n = int(input())
k = list(map(int, input().split()))
codes = []
for i in k:
    while i > 9:
        i = sum(int(j) for j in str(i))
    codes.append(i)

f = {}
for i in codes:
    f[i] = f.get(i, 0) + 1

max_f = max(f.values())
most_common_codes = min(c for c, count in f.items() if count == max_f)
print(*codes)
print(most_common_codes)
print(*[k[c] for c in range(n) if codes[c] == most_common_codes])

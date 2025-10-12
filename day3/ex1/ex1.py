with open("MINSEG.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

min_t = float('inf')

for i in range(n - 1):
    if a[i] > a[i + 1]:
        with open("MINSEG.OUT", "w") as f:
            f.write("-1")
        break
    else:
        for i in range(n - 1):
            t = a[i + 1] - a[i]
            if 0 < t < min_t:
                min_t = t

with open("MINSEG.OUT", "w") as f:
    if min_t == float('inf'):
        f.write("0")
    else:
        f.write(str(min_t))

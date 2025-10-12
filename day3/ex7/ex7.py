with open('PROMAX.INP', 'r') as f:
    t = int(f.readline())
    n = list(map(int, f.readline().split()))

n = sorted(n, reverse=True)
multi = n[0] * n[1] * n[2]

with open('PROMAX.OUT', 'w')  as f:
    f.write(str(multi))
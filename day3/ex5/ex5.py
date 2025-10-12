with open('SEQUENCE.INP', 'r') as f:
    t = int(f.readline())
    b = []
    for i in range(t):
        n = list(map(int, f.readline().split()))
        b.insert(n[0] - 1, n[1])
with open('SEQUENCE.OUT', 'w') as f:
    f.write(" ".join(str(_) for _ in b))
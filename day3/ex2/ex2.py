with open('LUYTHUA.INP', 'r') as f:
    t = int(f.readline())
    total = 0
    for i in range(t):
        n = int(f.readline().strip())
        base = n // 10 #vi du: 25 // 10 = 2 -> he so la 2
        exponent = n % 10 # vi duj: 25 % 10 = 5 -> so mux la 5
        total += base ** exponent
with open('LUATHUA.OUT', 'w') as f:
    f.write(str(total))
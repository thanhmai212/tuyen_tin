n = input().strip()
curr = n[0]
cmd = 2

for i in range(1, len(n)):
    if n[i] == curr:
        cmd += 1
    else:
        if i + 1 < len(n) and n[i + 1] == n[i]:
            cmd += 2
            curr = n[i]
        else:
            cmd += 2

print(cmd)
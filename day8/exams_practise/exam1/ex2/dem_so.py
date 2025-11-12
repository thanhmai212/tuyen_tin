with open('CNTNUM.INP', 'r') as f:
    n, q = map(int, f.readline().strip().split(" "))
    a = list(map(int, f.readline().strip().split(" ")))
    k = [int(f.readline()) for _ in range(q)]

ans = []
for i in k:
    qualiti = a[i - 1]
    left = a[0: i]
    right = a[i:]

    x = sum(1 for _ in left if _ == qualiti)
    y = sum(1 for _ in right if _ == qualiti)
    ans.append((x, y))

with open('CNTNUM.OUT', 'w') as f:
    for answer in ans:
        f.write(f"{answer[0]} {answer[1]}\n")
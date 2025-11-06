def build_zigzag(N):
    grid = [[0]*N for _ in range(N)]
    num = 1
    for s in range(2*N - 1):
        r_min = max(0, s - (N - 1)) 
        r_max = min(N - 1, s)
        coords = []
        for r in range(r_min, r_max + 1):
            c = s - r
            coords.append((r, c))
        if s % 2 == 0:
            coords.reverse()
        for (r, c) in coords:
            grid[r][c] = num
            num += 1
    return grid

N, K = map(int, input().split())
moves = input().strip()

grid = build_zigzag(N)
r = c = 0
total = grid[r][c]
print(total)
for mv in moves:
    if mv == 'U':
        r -= 1
    elif mv == 'D':
        r += 1
    elif mv == 'L':
        c -= 1
    elif mv == 'R':
        c += 1
    total += grid[r][c]

print(total)
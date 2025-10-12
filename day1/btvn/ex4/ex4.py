n, k = map(int, open("FLASHBACK.INP").read().split(" "))

total = n
level_1_count = n

for i in range(k):
    level_1_count = level_1_count * k
    total += level_1_count

with open("FLASHBACK.OUT", "w") as f:
    f.write(str(total))

n, m, k = map(int, open("BANH.INP").read().split(" "))
result = 0
if n > k:
    result = n * m - (n * m / 100 * 20)
else:
    result = n * m
with open("BANH.OUT", "w") as f:
    f.write(str(int(result)))
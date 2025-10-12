x, y, z = map(int, open("TBG.INP").read().split(" "))

t = (z * (x - y) + y - 1) // y

with open("TBG.OUT", "w") as f:
    f.write(str(t))
m, n = map(int, open("CLOCK.INP").read().split(" "))

re = (m + n) % 60
with open("CLOCK.OUT", "w") as f:
    f.write(str(re))

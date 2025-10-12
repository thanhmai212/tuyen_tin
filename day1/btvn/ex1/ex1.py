n, x = map(int, open("CHIPHI.INP").read().split(" "))
ghe = (n + 1) // 2
chi_phi = ghe * x

with open("CHIPHI.OUT", "w") as f:
    f.write(str(chi_phi))


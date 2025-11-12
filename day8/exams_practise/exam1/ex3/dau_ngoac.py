with open("CLUMSY.INP", 'r') as f:
    n = f.readline()
total = 0
for char in range(len(n) - 1):
    if n[char] == ")" and n[char + 1] == "(":
        total += 2
with open("CLUMSY.OUT", "w") as f:
    f.write(str(total))
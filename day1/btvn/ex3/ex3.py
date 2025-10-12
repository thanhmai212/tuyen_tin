weights = {'H': 1, 'O': 16, 'N': 14, 'C': 12}


def compute_mass(formula: str) -> int:
    i = 0
    n = len(formula)
    total = 0
    while i < n:
        ch = formula[i]
        i += 1

        if i < n and formula[i].isdigit():
            j = i
            while j < n and formula[j].isdigit():
                j += 1
            count = int(formula[i:j])
            print(count)
            i = j
            print(i)
        else:
            count = 1
        total += weights[ch] * count
    return total


with open('PHANTU.INP', 'r') as f:
    line = f.readline().strip()
mass = compute_mass(line)
with open('PHANTU.OUT', 'w') as f:
    f.write(str(mass))

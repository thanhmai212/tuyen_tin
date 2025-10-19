with open('PROMAX.INP', 'r') as f:
    t = int(f.readline())
    n = list(map(int, f.readline().split()))

negatives = []
positives = []

for num in n:
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)
negatives = sorted(negatives)
positives = sorted(positives, reverse=True)

if len(positives) >= 3:
    multi = positives[0] * positives[1] * positives[2]
else:
    if len(negatives) >= 2 and len(positives) >= 1:
        multi = negatives[0] * negatives[1] * positives[0]
    elif len(positives) >= 2 and len(negatives) >= 1:
        multi = positives[0] * positives[1] * negatives[0]
    else:
        multi = negatives[-1] * negatives[-2] * negatives[-3]

# n = sorted(n, reverse=True)
# multi = n[0] * n[1] * n[2]

with open('PROMAX.OUT', 'w')  as f:
    f.write(str(multi))
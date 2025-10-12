# S_mới của robot 1: S1_mới = S1 + V1 * t (t ở đây là thời gian đi)
# Tương tự với S2
# từ đây suy ra là nếu muốn Robot 1 và 2 gặp nhau thì: S1_mới == S2_mới
# hay S1 + V * t = S2 + V2 * t
# -> t = (S2 - S1) // (V1 - V2)

s1, v1, s2, v2 = map(int, open("DRP.INP").read().split(" "))
if v1 == v2:
    with open('DRP.OUT', 'w') as f:
        f.write(str(-1))
elif s1 < s2 and v1 < v2 or s2 < s1 and v2 < v1:
    with open('DRP.OUT', 'w') as f:
        f.write(str(-1))
else:
    t = (s2 - s1) // (v1 - v2)
    with open('DRP.OUT', 'w') as f:
        f.write(str(t))
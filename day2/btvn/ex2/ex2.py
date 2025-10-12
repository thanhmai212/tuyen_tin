with open("TAMGIAC.INP", "r") as f:
    t = int(f.readline())
    tests = [list(map(int, f.readline().split())) for i in range(t)]
result = []
for a, b, c in tests:
    if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
        result.append("0")
    else:
        if a < 90 and b < 90 and c < 90:
            result.append("NHON")
        elif a == 90 or b == 90 or c == 90:
            result.append("VUONG")
        # elif a == 60 and b == 60 and c == 60:
        #     result.append("CAN")
        else:
            result.append("TU")
with open("TAMGIAC.OUT", "w") as f:
    f.write("\n".join(result))

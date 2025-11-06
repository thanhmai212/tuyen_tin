import math

m, n = map(int, input().split(" "))
dogs = (n - 2 * m) / 2
chickens = m - dogs
if math.ceil(dogs) == int(dogs) and math.ceil(chickens) == int(chickens):
    print(f"Ga = {int(chickens)}")
    print(f"Cho = {int(dogs)}")
else:
    print("KHONG")

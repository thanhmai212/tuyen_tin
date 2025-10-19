m = int(input())
n = int(input())

dogs = (n - 2 * m) / 2
chickens = m - dogs

print(f"Chickens: {int(chickens)}")
print(f"Dogs: {int(dogs)}")

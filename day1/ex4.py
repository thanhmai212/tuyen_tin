n = list(map(int, input("Enter a list of integers: ").split(" ")))
total = 0

for i in n:
    if i % 2 != 0:
        total += i
print(f"Total of the odd in list: {total}")

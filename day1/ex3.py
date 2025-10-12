x = int(input("Enter x: "))
n = list(map(int, input("Enter n: ").split(" ")))
nums = 0

for i in n:
    if i >= x:
        nums += 1

print(f"Number of n greater than {x}: {nums}")
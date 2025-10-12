with open('BASE.INP', 'r') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
b = nums.copy()
for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        b.remove(nums[i])
with open('BASE.OUT', 'w') as f:
    f.write(f"{len(b)}" + "\n" + " ".join(str(x) for x in b))
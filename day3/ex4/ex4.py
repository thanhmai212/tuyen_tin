with open("BASE.INP", "r") as fi:
    n = int(fi.readline())
    nums = list(map(int, fi.readline().split()))
for i in range(n):
    for k in range(i):
        for l in range(i + 1, n - 1):
            if nums[k] > nums[i] < nums[l]:
                nums.remove(nums[i])
count = 0
for num in nums:
    count += 1
with open("BASE.OUT", "w") as fo:
    fo.write(str(count))
    fo.write("\n")
    for num in nums:
        fo.write(str(num) + " ")

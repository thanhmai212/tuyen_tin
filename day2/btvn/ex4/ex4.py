nums = list(map(int, open("QUES.INP").read().split(" ")))
nums = sorted(nums)

n = []

d1 = nums[1] - nums[0]
d2 = nums[2] - nums[1]

if d1 == d2:
    if nums[0] >= d1:
        n = [nums[2] + d1, nums[0] - d1]
else:
    if d1 > d2:
        n.append(nums[0] + d2)
    else:
        n.append(nums[1] + d1)
with open("QUES.OUT", "w") as f:
    f.write(" ".join(str(x) for x in sorted(n)))

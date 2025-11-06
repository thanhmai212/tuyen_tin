s = list(map(str, input().strip().split(" ")))
total_i = 0
highest_s = s[0]
list_highest_s = []
for i in s:
    if i == '' or i == ' ':
        total_i += 1
    if len(i) >= len(highest_s):
        highest_s = i

print(len(s) - total_i)
print(len(highest_s))
print(*[_ for _ in s if len(_) == len(highest_s)])
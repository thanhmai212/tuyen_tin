import collections

n = int(input())
list_n = list(map(int, input().split(" ")))
k = int(input())
print(*sorted(list_n))

if k > n:
    print("KHONG")
else:
    count = collections.Counter(list_n)
    results = sorted([n for n in count if count[n] >= k])
    print(*results) if results else print("KHONG")

n = int(input())
k = sorted(map(int, input().split(" ")))
print(*k)
k = [num + 5 if num % 2 != 0 else num - 3 for num in k]
k.sort(reverse=True)
print(*k)
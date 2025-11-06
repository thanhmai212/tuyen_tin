n = int(input())
list_n = list(map(int, input().split(" ")))

print(sum(int(_) for _ in list_n if _ % 2 == 0))
print(max(list_n), list_n.index(max(list_n)) + 1)
print(min(list_n), list_n.index(min(list_n)) + 1)


def is_increase(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True


print("DAY TANG" if is_increase(list_n) else "DAY KHONG TANG")

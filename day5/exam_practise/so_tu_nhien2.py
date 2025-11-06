n = int(input().strip())
list_n = [_ for _ in str(abs(n))]
list_n.sort(reverse=True)
print(sum(1 for i in range(1, n + 1) if n % i == 0))
print(sum(1 for _ in str(abs(n))))
print(list_n[0])
print(f"{list_n[0]}{list_n[1]}{list_n[2]}")



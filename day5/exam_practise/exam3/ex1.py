n = int(input())

def is_gcd_n(n):
    for i in range(1, n + 1):
        if n % i == 0:
            return True
        return False

print(sum(1 for num in range(1, n + 1) if is_gcd_n(num)))
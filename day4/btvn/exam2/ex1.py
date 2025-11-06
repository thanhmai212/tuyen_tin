def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n**0.5 + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

digital = len(str(abs(n)))
sum_digital = sum(int(num) for num in str(abs(n)))
min_prime = max([_ for _ in range(n) if is_prime(_)])
max_prime = min([_ for _ in range(n + 1, 2*n) if is_prime(_)])
prime_nearest_n = min_prime if max_prime - n > n - min_prime else min_prime if max_prime - n == n - min_prime else max_prime

print(digital)
print(sum_digital)
print(sum(int(_) for _ in range(n) if is_prime(_)))
print(prime_nearest_n)

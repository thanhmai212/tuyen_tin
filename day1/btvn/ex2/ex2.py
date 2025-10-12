import sympy

l, n = map(int, open("PASSWORD.INP").read().split(" "))

password = []

for i in range(l, n + 1):
    if sympy.isprime(i):
        if sympy.isprime(sum(int(a) for a in str(i))):
            password.append(i)

with open("PASSWORD.OUT", "w") as f:
    f.write(str(password))

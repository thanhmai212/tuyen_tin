a = int(input())
b = int(input())
c = int(input())
if a == b + c:
    print(f'{a}={b}+{c}')
elif c == a + b:
    print(f'{a}+{b}={c}')
elif a == b * c:
    print(f'{a}={b}*{c}')
elif c == a * b:
    print(f'{a}*{b}={c}')
else:
    print("NO")
s = input()

print(sum(int(_) for _ in s if _.isdigit()))
s1 = ''.join(_ for _ in s if not _.isdigit())
print(s1)
if len(s1) > 0:
    s2 = s1[0]
    for i in range(1, len(s1)):
        if s1[i] != s1[i - 1]:
            s2 += s1[i]
    print(s2)
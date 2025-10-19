s = input()
a = []
index_final = -1

temp = ""
total = 0

for i in s:
    if i.isdigit():   
        a.append(i)
print(f"a = {"".join(_ for _ in a)}")
        
for num in range(len(a)):
    if a[num] == "5" or a[num] == "0":
        index_final = num        
if index_final == -1:
    print("KHONG")
else:
    b = a[0: index_final + 1]

for o in range(len(s)):
    if s[o].isdigit():
        temp = temp + s[o]
    else:
        if temp != "":
            temp = int(temp)
            total += temp
            temp = ""
if temp != "":
    temp = int(temp)
    total += temp                    

print(f"b = {"".join(_ for _ in b)}")
print(f"t = {total}")
n = int(input())
woods = list(map(int, input().split(" ")))
k_input = int(input())
woods.sort()
total_cut = 0
shortest_wood = woods[0]
for wood in woods:
    if wood != shortest_wood:
        total_cut += wood - shortest_wood
total_of_cutting_wood = 0
list_h = []

for i in range(20):
    for w in woods:
        temp = w - i
        if temp < 0:
            temp = 0
        total_of_cutting_wood += temp
    if total_of_cutting_wood >= k_input:
        list_h.append(i)
    total_of_cutting_wood = 0
print(total_cut)
print(max(list_h))

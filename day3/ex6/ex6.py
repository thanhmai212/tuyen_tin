list_y = []
list_x = []

with open("RECT.INP", "r") as f:
    n = int(f.readline())
    for _ in range(n):
        y, x = map(int, f.readline().split())        
        list_y.append(y)
        list_x.append(x)
        
s_rectangle = (max(list_x) - min(list_x)) * (max(list_y) - min(list_y))
with open("RECT.OUT", "w") as f:
    f.write(str(s_rectangle))
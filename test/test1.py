li = ["Apple",121,"cool",55]
l = []
x=0
for i in li:
    if isinstance(i,int):
        l.append(i)
        li.pop(x)
    x += 1

li
l

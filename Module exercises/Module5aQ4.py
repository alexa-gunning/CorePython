data = [12, -5, -6, 8]
list2 = []
for num in data:
    if num < 0:
        num = num * -1
        list2.append(num)
    elif num>0:
        num = num
        list2.append(num)
print(list2)

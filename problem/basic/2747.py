lst = [0,1]
for i in range(2,46):
    lst.append(lst[i-2]+lst[i-1])

print(lst[int(input())])
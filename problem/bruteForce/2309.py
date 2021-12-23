lst = []
for i in range(9):
    lst.append(int(input()))

for i in range(9):
    for j in range(i+1,9):
        if sum(lst)-(lst[i]+lst[j]) == 100 and lst[i] != lst[j]:
            num1 = lst[i]
            num2 = lst[j]
lst.remove(num1)
lst.remove(num2)
            
lst.sort()        
for i in lst:
    print(i)
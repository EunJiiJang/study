n = int(input())
lst =[]
fibo = [0,1]
for i in range(2,46):
    fibo.append(fibo[i-1]+fibo[i-2])
for _ in range(n):
    lst.append(int(input()))

for i in range(n):
    num = lst[i]
    rst=[]
    for j in range(45,0,-1):
        if fibo[j] <= num:
            rst.append(fibo[j])
            num = num - fibo[j]

            if num == 0:
                rst.sort()
                for result in rst:
                    print(result, end=" ")
                    
                
                break
    print()

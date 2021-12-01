coin =[500,100,50,10,5,1]
n = int(input())

sum = 1000 - n
cnt = 0 
for i in coin:
    num = sum // i
    sum -= num * i
    cnt += num 

print(cnt)
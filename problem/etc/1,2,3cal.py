n = int(input())
a = []   
for j in range(n):
   a.append(int(input()))
count = 0 
num = [1,2,4]
for i in range(3,20):
    num.append(num[i-3]+num[i-2]+num[i-1])
for i in a:
    print(num[i-1])
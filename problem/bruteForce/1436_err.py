n = int(input())
lst = []


chk = 0
num=666

while True:
    if n == chk:
        print(lst[n-1])
        break
    else:
        cnt = 0
        for j in str(num):
            if j == '6':
                cnt += 1
                if cnt >= 3:
                    lst.append(num)
                    chk += 1
                    break    
    num += 1

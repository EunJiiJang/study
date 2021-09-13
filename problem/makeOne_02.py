#시간초과
#메모이제이션
n = int(input())
cnt = 0
while n >= 0 :
    if n % 3 == 0:
        n = (n//3)
        cnt += 1
    elif n % 2 == 0:
        n = (n//2)
        cnt += 1
    else :
        n -= 1
        cnt += 1
    if n == 1:
        print(cnt)
        break
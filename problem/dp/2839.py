value = int(input())

cnt = 0
while value >= 0:
    if value % 5 == 0:
        cnt += value//5
        print(cnt)
        break
    value -= 3
    cnt += 1
else:
    print(-1)
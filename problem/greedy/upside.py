n = input()
cnt = 0
prev = '?'
for i in n:
    if i != prev:
        prev = i
        cnt += 1
print((cnt)//2)

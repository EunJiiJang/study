n = list(input())
sum = 0
n.sort(reverse=True)
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

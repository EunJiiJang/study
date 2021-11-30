n = int(input())
s = [1]*10
for i in range(n-1):
    for j in range(1, 10):
        s[j] += s[j-1]

print(sum(s)%10007)
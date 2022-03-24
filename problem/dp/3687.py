from cgitb import small


2554563766
num  = int(input())
number  = [int(input()) for i in range(num )]

for i in range(len(number)):
    ans_max = '7' * (number[i]%2)+'1'*(number[i]//2-(number[i]%2))

    ans = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    n = number[i]
    if n <= 10:
        ans_min = ans[n]
    else:
        ans_min = ''
        while n > 0:
            n -= 7
            if n >= 0:
                ans_min +='8'
            else:
                n+=7
                break
        small = {2:'1', 5:'2', 6:'6'}
        if n in small:
            ans_min = small[n] + ans_min
        else:
            if n == 1:
                ans_min = '10'+ans_min[1:]
            elif n == 3:
                ans_min = '200'+ans_min[2:]
            elif n == 4:
                ans_min = '20' + ans_min[1:]

    print(ans_min, end=' ')
    print(ans_max)
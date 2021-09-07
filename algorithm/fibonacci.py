def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1)+fibo(num-2)
     
print(fibo(10))
##동적계획법
def fibo_dp(num):
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for idx in range(2,num+1):
        cache[idx] = cache[idx - 1] + cache[idx - 2]
    return cache[num]


print(fibo_dp(10))
def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

for n in range(10):
    print(factorial(n))


def sum_list(data):
    if len(data) <=1:
        return data[0]
    return data[0] + sum_list(data[1:])

import random

data = random.sample(range(100),10)
print(sum_list(data))


def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
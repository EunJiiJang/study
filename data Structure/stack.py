##마지막으로 넣은 데이터 먼저 out
##stack 체험
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
data_stack.pop()
print(data_stack)

##list를 통해 stack 구현
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data 

for index in range(10):
        push(index)

print(pop())
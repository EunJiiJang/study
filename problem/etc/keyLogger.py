n = int(input())

for _ in range(n):
    leftS,rightS = [],[]
    data = input()
    for i in data:
        if i == '-':
            if leftS:
                leftS.pop()
        elif i == '<':
            if leftS:
                rightS.append(leftS.pop())

        elif i == '>':
            if rightS:
                leftS.append(rightS.pop())
        else:
            leftS.append(i)
    leftS.extend(reversed(rightS))
    print(''.join(leftS))
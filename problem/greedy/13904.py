lst = []
n =int(input())
for i in range(n):
    lst.append(list(map(int,input().split(' '))))

lst.sort(key= lambda x:-x[1])
result = [0]*1000
#정렬 후 가장 점수를 많이 주는 과제의 최대한 미룰 수 있는 일자에 배치
for i in range(n):
    for j in range(lst[i][0]-1,-1,-1):
        if result[j] == 0:
            result[j] = lst[i][1]
            break

print(sum(result))

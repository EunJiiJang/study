grid = [[1,8,3,2],[7,4,6,5]]

dx = [1,  0]
dy = [0,  1]
q = [[0,0]]
def solution2(grid):
    answer = 0
    lst = []
    route = []
    m,n = len(grid),len(grid[0])
    route.append(grid[0][0])
    while q:
        i, j = q[0][0], q[0][1]
        del q[0]
        if i == m-1 and j == n-1:
            lst.append(sum(route))
        else:
            for t in range(2):
                x = i + dx[t]
                y = j + dy[t]
                if 0 <= x < m and 0 <= y < n:
                    q.append([x, y])
                    route.append(grid[i][j])
                
            # route.pop()
                

            # if 0 <= i + 1 < m and 0 <= j + 1 < n:
            #     q.append([i, j])
            #     route.append(grid[i][j])
            # route.pop()
    answer = min(lst) 
    print(answer)  
    return answer

print(solution2(grid))
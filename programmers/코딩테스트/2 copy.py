grid = [[1,2],[3,4]]


def findPath(grid,route = [],i=0, j=0):
    global answer
    m,n = len(grid),len(grid[0])
    route.append(grid[i][j])
    if i == m-1 and j == n-1:
        
        print(route)
        
    else:
        if i + 1 < m:
            solution(grid, route, i+1, j)

        if j + 1 < n:
            solution(grid, route, i, j + 1)
    route.pop()
    lst = []
    for num in range(len(route)):
        lst.append(sum(route[num]))
    answer = min(lst)
    return answer
   
def solution(grid):
    global answer
    answer = 0
    route = []
    findPath(grid,route,i=0, j=0)
    return answer
    

solution(grid)
# solution(grid)
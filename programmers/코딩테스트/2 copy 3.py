grid = [[1,8,3,2],[7,4,6,5]]

lst = []
def findPath(grid,route = [],i=0, j=0):
    m,n = len(grid),len(grid[0])
    route.append(grid[i][j])
    
    if i == m-1 and j == n-1:
        lst.append(sum(route))
    else:
        if i + 1 < m:
            findPath(grid, route, i+1, j)

        if j + 1 < n:
            findPath(grid, route, i, j + 1)
    route.pop()
   
    
   
def solution(grid):

    findPath(grid)
    answer = 0
    answer = min(lst)
   
    return answer

print(solution(grid))
# solution(grid)
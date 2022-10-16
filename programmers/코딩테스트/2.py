grid = [[1,2],[3,4]]

dx = [1,  0]
dy = [0,  1]
q = [[0,0]]
visit = []
def solution(grid):
    n , m = len(grid),len(grid[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    while q:
        a, b = q[0][0], q[0][1]
        del q[0]
        for i in range(2):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                q.append([x, y])
                grid[x][y] = grid[a][b] + grid[x][y]
    answer = grid[len(grid)-1][len(grid[0])-1]
    return answer

print(solution(grid))
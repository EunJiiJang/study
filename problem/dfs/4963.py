dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i,j):
  board[i][j] = 0
  q = [[i,j]]
  while q:
    a,b = q[0][0],q[0][1]
    del q[0]
    for k in range(8):
      x = a + dx[k]
      y = b + dy[k]
      if 0 <= x < h and 0 <= y < w and board[x][y] == 1:
                board[x][y] = 0
                q.append([x, y])
      
while True:
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  board = []
  cnt = 0
  for i in range(h):
    board.append(list(map(int,input().split())))
  for i in range(h):
    for j in range(w):
      if board[i][j] ==1:
        bfs(i,j)
        cnt += 1
  print(cnt)
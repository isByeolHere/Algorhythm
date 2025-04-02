import sys
input = sys.stdin.readline
from collections import deque

# 익으면 1, 익지않으면 0, 없으면 -1
#m가로 n세로 h상자수
m, n, h = map(int, input().split())


matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] *m for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 일단 익은 토마토를 큐에 넣어
q = deque()
ans = 0

def bfs():
  while q:
    z, y, x = q.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
          continue
      
      if matrix[nz][ny][nx]== 0 and not visited[nz][ny][nx]:
        q.append((nz, ny, nx))
        matrix[nz][ny][nx] = matrix[z][y][x] + 1
        visited[nz][ny   ][nx] = True

# 탐색
for i in range(h):
  for ii in range(n):
    for iii in range(m):
      if matrix[i][ii][iii] == 1 and not visited[i][ii][iii]:
        q.append((i,ii,iii))
        visited[i][ii][iii] = True

bfs()

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        ans = max(ans, max(b))

print(ans-1)
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ice = []

for i in range(n):
  for ii in range(m):
    if graph[i][ii]:
      ice.append((i,ii))

# R D L U
dx = [1, 0, -1, 0]
dy = [0, -1, 0 , 1]
year = 0

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1
  sea_list = []

  while q:
    x, y = q.popleft()
    sea = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m :
        if not graph[nx][ny]:
          sea += 1
        elif graph[nx][ny] and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = 1
    if sea > 0:
      sea_list.append((x, y, sea))
  
  for x, y, sea in sea_list:
    graph[x][y] = max(0, graph[x][y] - sea)
  
  return 1


while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, ii in ice:
        if graph[i][ii] and not visited[i][ii]:
            group += bfs(i, ii)
        if graph[i][ii] == 0: # 탐색이 끝나면 바다가 된 빙산을 체크
            delList.append((i, ii))
    if group > 1: # 빙산그룹이 2개 이상이면 년을 출력
        print(year)
        break
    
    # 다 녹은 빙산은 탐색할 필요가 없으므로 ice에서 제거
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)
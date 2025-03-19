# 안전 영역

import sys
from collections import deque

def bfs(i,j, high):
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        # queue는 지금 주변이 어디까지 붙어있나 봄
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if height[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))


n = int(sys.stdin.readline())

height= []
max_height = 0

for i in range(n):
  height.append(list(map(int, sys.stdin.readline().split())))
  for j in range(n):
    if height[i][j] > max_height:
      max_height = height[i][j]

dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]
queue = deque()
result = 0

for k in range(max_height):
    visited = [[0] * n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if height[i][j] > k and visited[i][j] == 0:
                bfs(i,j, k)
                ans += 1 
    
    if result < ans:
        result = ans
print(result)
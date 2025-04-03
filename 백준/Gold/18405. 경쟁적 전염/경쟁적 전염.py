import sys
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int,input().split())
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q= []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
          heapq.heappush(q,(0, graph[i][j], i, j))

while q:
    time, virus, x, y = heapq.heappop(q)

    if time == s:
      break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                heapq.heappush(q, (time + 1, virus, nx, ny))

print(graph[target_x - 1][target_y - 1])
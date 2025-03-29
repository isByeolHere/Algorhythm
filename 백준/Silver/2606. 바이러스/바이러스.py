import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

com = int(input().strip())
edge = int(input().strip())
graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for i in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


bfs(1)
print(visited.count(True)-1)

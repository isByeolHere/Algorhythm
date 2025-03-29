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

# for i in range(1, com+1):
#   if not visited[i]:
bfs(1)

cnt=0
for i in visited:
  if i == True:
    cnt+=1

print(cnt-1)
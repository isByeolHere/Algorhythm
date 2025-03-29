import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
# 간선 입력처리
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited1 = [0] *(n+1)
visited2 = visited1.copy()

# 그래프는 2차원 배열
# visited는 리스트
def dfs(v):
  visited1[v] = True
  print(v, end=" ")
  
  for i in sorted(graph[v]):
    if not visited1[i]: 
      dfs(i)


def bfs(v):
  queue = deque([v])
  visited2[v] = True
  while queue:
    cur = queue.popleft()
    print(cur, end=" ")
    for i in sorted(graph[cur]):
      if not visited2[i]: 
          queue.append(i)
          visited2[i] = True

dfs(v)
print()
bfs(v)

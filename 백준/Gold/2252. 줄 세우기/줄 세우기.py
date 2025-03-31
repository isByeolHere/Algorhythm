import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
queue = deque()

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  degree[b] += 1

for i in range(1, n+1):
  if degree[i] == 0:
    queue.append(i)

box = []
while queue:
  target = queue.popleft()
  box.append(target)
  for i in graph[target]:
    degree[i] -= 1
    if degree[i] == 0:
      queue.append(i)

print(*box)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)


def dfs(node):
  visited[node] = 1
  for i in graph[node]:
    if not visited[i]:
      parent[i] = node
      dfs(i)

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

dfs(1)

print(*parent[2:], sep='\n')
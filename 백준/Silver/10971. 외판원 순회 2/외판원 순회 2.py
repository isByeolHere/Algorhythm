
# 외판원 순회
import sys

def travel(cnt, start, now, cost):
  global min_price

  if cnt == n and city[now][start] :
      cost += city[now][start]
      if cost < min_price:
        min_price = cost
        return

  for i in range(n):
    if not visited[i] and city[now][i]:
      visited[i] = True
      travel(cnt+1, start, i, cost+city[now][i])
      visited[i] = False

n = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n
min_price = sys.maxsize

for i in range(n):
    visited[i] = True
    travel(1, i, i, 0)
    visited[i] = False

print(min_price)
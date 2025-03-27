
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  prime = list(map(int, input().split()))

  queue = deque()

  for i in range(n):
    queue.append((prime[i], i))

  cnt = 0

  while queue :
    cur_priority, cur_index = queue.popleft()

    if any(cur_priority < other for other, _ in queue) :
      queue.append((cur_priority, cur_index))

    else:
      cnt += 1
      if cur_index == m:
        print(cnt)
        break
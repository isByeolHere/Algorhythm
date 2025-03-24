import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
queue = deque()
nk = []

for i in range(1, n+1):
  queue.append(i)

while queue:
  for j in range(k-1):
    tmp = queue.popleft()
    queue.append(tmp)
  tmp = queue.popleft()
  nk.append(tmp)

print("<" + ", ".join(map(str, nk)) + ">")
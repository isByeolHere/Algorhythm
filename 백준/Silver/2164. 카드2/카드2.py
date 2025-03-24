import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(1, n+1):
  queue.append(i)


while len(queue) > 1 :
  queue.popleft()
  tmp = queue.popleft()
  queue.append(tmp)


print(queue.popleft())

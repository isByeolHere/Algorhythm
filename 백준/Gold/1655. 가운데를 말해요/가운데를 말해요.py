import heapq 
import sys
input = sys.stdin.readline

left_h = []
right_h = []

mid = 0
n = int(input())
mid = int(input())
print(mid)

for i in range(1, n):
  num = int(input())
  if num > mid :
    heapq.heappush(right_h, num)
    if len(left_h) + 1 < len(right_h):
      heapq.heappush(left_h, (-mid, mid))
      mid = heapq.heappop(right_h)
  else: 
    heapq.heappush(left_h, (-num, num))
    if len(right_h) < len(left_h):
      heapq.heappush(right_h, mid)
      mid = heapq.heappop(left_h)[1]
  print(mid)

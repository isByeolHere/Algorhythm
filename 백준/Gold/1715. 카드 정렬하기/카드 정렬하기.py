import sys, heapq
input= sys.stdin.readline

n = int(input())
cards = []

for i in range(n):
  a = int(input())
  heapq.heappush(cards, a)

result = 0
while len(cards) > 1:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  sum = a+b
  result += sum
  heapq.heappush(cards, sum)

print(result)
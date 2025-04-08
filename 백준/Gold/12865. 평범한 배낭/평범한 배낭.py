import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = []
for _ in range(n):
  w, v = map(int, input().split())
  items.append((w, v))
dp = [0] * (k+1)
for item in items:
  w,v = item
  for i in range(k, w-1, -1):
    dp[i] = max(dp[i], dp[i-w]+v)
print(dp[-1])
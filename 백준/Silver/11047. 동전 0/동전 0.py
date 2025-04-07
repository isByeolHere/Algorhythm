import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = []
for _ in range(n):
  coins.append(int(input().strip()))
ans = 0
coins.sort(reverse=True)

for coin in coins:
  if k >= coin:
    ans += k // coin
    k %= coin
    if k <= 0:
      break

print(ans)
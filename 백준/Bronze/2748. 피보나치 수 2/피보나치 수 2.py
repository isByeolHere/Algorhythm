import sys
input = sys.stdin.readline

n = int(input().strip())
ans = []
ans.append(0)
ans.append(1)

for i in range(2, n+1):
  ans.append(ans[i-1]+ans[i-2])
print(ans[n])
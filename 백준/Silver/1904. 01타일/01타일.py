import sys
input = sys.stdin.readline
n = int(input().strip())
ans = []
ans.append(0)
ans.append(1)
ans.append(2)
div = 15746
for i in range(3,n+1):
  tmp = (ans[i-1]+ans[i-2])%div
  ans.append(int(tmp))

print(ans[n])
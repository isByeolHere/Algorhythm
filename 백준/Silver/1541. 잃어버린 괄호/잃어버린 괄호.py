import sys
input = sys.stdin.readline
n = input().split('-')

num = []
for i in n:
  sum = 0
  tmp = i.split('+')
  for j in tmp:
    sum += int(j)
  num.append(sum)

ans = num[0]

for i in range(1,len(num)):
  ans -= num[i]

print(ans)
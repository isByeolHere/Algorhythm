import sys

n, m = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

start = 0
last = max(trees)
h = 0
while start <= last :
  sum_tree = 0
  pr = (start+last) // 2
    
  for i in trees:
    if i > pr:
      sum_tree += i - pr

  if sum_tree < m:
    last = pr-1

  else:
    h = pr
    start = pr+1

print(h)
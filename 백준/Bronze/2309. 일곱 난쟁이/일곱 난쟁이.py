import sys

smalls = list(map(int, sys.stdin.read().split()))

height = 0

for i in range(8):
  if height == 100:
    break
  for j in range(i+1,9):
    if sum(smalls) - smalls[i] - smalls[j] == 100: 
      height = 100
      fake1 = smalls[i]
      fake2 = smalls[j]
      smalls.remove(fake1)
      smalls.remove(fake2)
      break

smalls.sort()
for i in range(7):
  print(smalls[i])

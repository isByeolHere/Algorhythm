import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
count = 0

for x in A:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        count += 1
      break

print(count)
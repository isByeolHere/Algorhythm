import sys

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
nums.sort()

for j in nums:
  print(j)
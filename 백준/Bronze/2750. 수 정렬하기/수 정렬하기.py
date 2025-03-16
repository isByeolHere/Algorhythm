import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.read().split()))

num_ascend = []

for i in range(len(nums)):
  a = min(nums)
  num_ascend.append(a)
  nums.remove(a)

for i in num_ascend:
  print(i)
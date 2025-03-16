import sys

input = sys.stdin.readline

n = int(input())

a = [0] * 10001

for num in range(n):
  num = int(input())
  a[num] += 1

for i in range(10001):
  if a[i] != 0:
    for j in range(a[i]):
      print(i)
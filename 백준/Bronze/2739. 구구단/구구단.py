import sys

a = int(sys.stdin.readline().strip())
# input()
for i in range(1, 10, 1):
  print(f"{a} * {i} = {a * i}")
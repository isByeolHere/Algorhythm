import sys

a, b = map(int, sys.stdin.readline().split())

def change(num):
  num_to_str = str(num)
  swap = num_to_str[2] + num_to_str[1] + num_to_str[0]
  return int(swap)

print(max(change(a), change(b)))
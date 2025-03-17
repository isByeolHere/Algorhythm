import sys

n = int(sys.stdin.readline())

def get_fact(n: int):
  if n > 0:
    return n * get_fact(n-1)
  else:
    return 1

print(get_fact(n))
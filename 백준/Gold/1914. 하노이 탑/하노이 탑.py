import sys

def Hanoi(n, a, b, c):
  if n == 1:
    print(a, c)
    return
  
  Hanoi(n-1, a, c, b)
  print(a, c)
  Hanoi(n-1, b, a, c)

n = int(sys.stdin.readline())

print(2 ** n -1)
if n <= 20:
  Hanoi(n, 1, 2, 3)
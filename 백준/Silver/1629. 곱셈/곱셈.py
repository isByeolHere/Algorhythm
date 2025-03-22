import sys

def reduce(a, b ,c):
  if b == 1:
    return a % c
  
  X = reduce(a, b//2, c)
  # 짝수라면
  if b % 2 == 0:
    return X * X % c
  # 홀수라면
  else:
    return a * X * X % c
  

a, b, c = map(int, sys.stdin.readline().split())

print(reduce(a,b,c))

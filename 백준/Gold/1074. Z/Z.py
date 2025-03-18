import sys

def check(n, r, c):
  half = 2 ** (n-1)
  if n == 1:
    return 2*r+c
  elif r < half and c < half:
    return check(n-1,r,c)
  elif r < half and c >= half:
    return half**2 + check(n-1,r,c-half)
  elif r >= half and c < half:

    return half**2*2 + check(n-1,   r-half, c)
  else:
    return half**2*3 + check(n-1,r-half,c-half)

n, r, c = list(map(int, sys.stdin.readline().split()))
a = check(n, r, c)
print(a)
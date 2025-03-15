import sys

def is_prime(A):
  if A < 2:
    return False
  for i in range(2, A):
    if A % i == 0:
      return False
  return True

T = int(sys.stdin.readline())
for _ in range(T):
    P = int(sys.stdin.readline())

    B = P // 2
    C = P // 2

    for _ in range(P // 2):
      if is_prime(B) and is_prime(C):
        print(B, C)
        break
      else:
        B -= 1
        C += 1
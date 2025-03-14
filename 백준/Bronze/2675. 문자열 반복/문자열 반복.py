# 문자열 반복
import sys

t = int(sys.stdin.readline().strip()) # 테스트 횟수

for _ in range(t):
  r, s = sys.stdin.readline().split()
  r = int(r)
  for x in s:
    print(x * r, end="")
  print()
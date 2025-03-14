import sys

c = int(sys.stdin.readline().strip())

for _ in range(c):
  a = list(map(int, sys.stdin.readline().split()))
  n = a[0]
  scores = a[1:n+1]

  average = sum(scores) / n

  count_high = sum(1 for score in scores if score > average) 

  percentage = (count_high / n) * 100

  print(f"{percentage:.3f}%")
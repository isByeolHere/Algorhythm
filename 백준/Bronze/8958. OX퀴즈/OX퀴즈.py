import sys

a = int(sys.stdin.readline().strip())

for _ in range(a):
  b = sys.stdin.readline().strip()
  score = 0
  sumScore = 0
  for j in b:
    if j == 'O':
      score += 1
      sumScore += score
    else:
      score = 0
    
  print(sumScore)
import sys

def is_hansu(a):
  a_list = list(map(int, str(a)))
  if len(a_list) <= 2:
    return True
  diff = a_list[1] - a_list[0]
  for i in range(1, len(a_list) - 1):
    if a_list[i+1]-a_list[i] != diff:
      return False
  return True

n = int(sys.stdin.readline())

count = 0

for j in range(1, n+1):
  if is_hansu(j):
    count += 1

print(count)
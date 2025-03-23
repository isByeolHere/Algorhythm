import sys
n = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

start = 0
end = n-1

dif = abs(liquids[start] + liquids[end])

new_start = start
new_end = end

while start < end:

  total = liquids[start] + liquids[end]

  if abs(total) < dif :
    dif = abs(total)
    new_start = start
    new_end = end

    if dif == 0:
      break
  if total > 0 :
    end -= 1
  else:
    start += 1

print(liquids[new_start], liquids[new_end])
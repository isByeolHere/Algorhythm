# 종이자르기

import sys

h, v = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

a_list = [0, h]
b_list = [0, v]

for _ in range(n):
  cut_times = list(map(int, sys.stdin.readline().split()))
  if cut_times[0] == 0:
    b_list.append(cut_times[1])
  else:
    a_list.append(cut_times[1])

a_list.sort()
b_list.sort()

max_width = max(a_list[i] - a_list[i-1] for i in range(1, len(a_list)))
max_height = max(b_list[i] - b_list[i-1] for i in range(1, len(b_list)))

largest =  max_width * max_height

print(largest)

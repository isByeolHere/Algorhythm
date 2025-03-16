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
largest = 0

for i in range(1, len(a_list)):
  for j in range(1, len(b_list)):
    width = a_list[i] - a_list[i-1]
    height = b_list[j] - b_list[j-1]
    a = width * height
    largest = max(largest, a)

print(largest)
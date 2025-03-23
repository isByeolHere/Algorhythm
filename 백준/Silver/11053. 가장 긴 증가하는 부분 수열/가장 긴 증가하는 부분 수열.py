
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def bin_search(arr, target):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start+end) // 2

    if arr[mid] < target:
      start = mid + 1

    else:
      end = mid - 1
  return start

lis = [a[0]]
for i in range(1, len(a)):
  if a[i] > lis[-1]:
    lis.append(a[i])
  else:
    new_index = bin_search(lis, a[i])
    lis[new_index] = a[i]

print(len(lis))
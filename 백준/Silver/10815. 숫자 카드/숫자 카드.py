import sys
input = sys.stdin.readline

# 상근 카드
n = int(input())
a = list(map(int, input().split()))

# 상근이가 가지고 있는 카드인지 아닌지 확인할 숫자
m = int(input())
b = list(map(int, input().split()))
a.sort()

def bin_search(arr, target):
  pl = 0
  pr = len(arr)-1

  while pl <= pr:
    pc = (pl+pr) // 2

    if arr[pc] == target:
      return 1
    elif arr[pc] > target:
      pr = pc - 1
    else:
      pl = pc + 1
  return 0

for i in range(m):
  print(bin_search(a, b[i]), end=" ")
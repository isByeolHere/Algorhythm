
import sys

def total(n, arr, x, y):
    total_sum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            total_sum += arr[i][j]
    return total_sum

def check_square(n, arr, x, y):
  global cnt_white
  global cnt_blue

  if n == 1:
    if arr[x][y] == 0:
      cnt_white += 1
    else:
      cnt_blue += 1
    return

  area_sum = total(n, arr, x, y) 

  if area_sum == n*n :
    cnt_blue += 1
    # print(cnt_blue, cnt_white)
  elif area_sum == 0:
    cnt_white += 1
    # print(cnt_blue, cnt_white)
  else:
    half = n//2
    # print(cnt_blue, cnt_white)
    check_square(half, arr, x, y)
    check_square(half, arr, x, y+half)
    check_square(half, arr, x+half, y)
    check_square(half, arr, x+half, y+half)


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt_white = 0
cnt_blue = 0

check_square(n, arr, 0, 0)

print(cnt_white)
print(cnt_blue)



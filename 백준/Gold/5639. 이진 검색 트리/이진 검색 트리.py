import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

arr = []
while True:
  try:
    node = int(input())
  except:
    break
  arr.append(node)


def post_order(root_idx, last_idx):
  if root_idx > last_idx:
    return
  
  root = arr[root_idx]

  right_start_idx = root_idx + 1
  while right_start_idx <= last_idx:
    if arr[right_start_idx] > root:
        break
    right_start_idx += 1

  post_order(root_idx + 1, right_start_idx - 1)
  post_order(right_start_idx, last_idx)
  print(root)

post_order(0, len(arr) - 1)
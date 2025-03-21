import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
## 코드 공부 후

def binary_search(target, a):
    
  pl = 0
  pr = len(a)-1
  
  # 찾을 때 까지 반복 못찾으면 종료
  while pl <= pr:
    pc = (pl+pr) // 2
    # 반짤랐는데 타겟이 바로 나옴.
    if target == a[pc]:
      return 1
    # 반짤랐는데 타겟이 왼쪽에 있음.
    elif target < a[pc]:
      pr = pc - 1
    # 반짤랐는데 타겟이 오른쪽에 있음.
    else:
      pl = pc + 1
  return 0

for i in range(len(b)):
  print(binary_search(b[i], a))


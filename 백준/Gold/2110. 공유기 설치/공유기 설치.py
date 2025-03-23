import sys
n, c = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for i in range(n)]
x.sort()

start = 1
end = x[-1]-x[0]
min_distance = (start+end) // 2

while start <= end:

  # 일단 제일첫번째 설치 후 
  # mid만큼 두고 설치했을 때 몇개 설치할 수 있는지 센다
  tmp = x[0]
  cnt = 1
  for i in range(1, n):
    # 처음꺼보다 min_distance 거리만큼 갔는데 다음 집보다 덜갔어? 그럼 
    if tmp+min_distance <= x[i]:
      cnt += 1
      tmp = x[i]

  if cnt < c:
    end = min_distance - 1
  else:
    # result = min_distance
    start = min_distance + 1
  min_distance = (start+end) // 2

print(min_distance)
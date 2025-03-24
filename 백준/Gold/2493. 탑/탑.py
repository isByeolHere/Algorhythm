import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))


stack = []
ans = [0] * n

# 스택에 (타워인덱스, 높이) 튜플로 저장
for i in range(n):
  while stack:
    # 최고 탑 높이가 지금 기준탑보다 크면 레이저 쏘임
    if tops[stack[-1]-1] > tops[i]:
      ans[i] = stack[-1]
      break
    else:
    #최고 탑 높이가 지금 기준탑보다 더 낮으면 
      stack.pop()
  # (타워인덱스, 높이)를 스택에 저장
  stack.append(i + 1)

print(*ans)
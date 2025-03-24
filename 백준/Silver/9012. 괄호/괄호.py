import sys

t = int(sys.stdin.readline())
for i in range(t):
  test = sys.stdin.readline().strip()
  

  stack = []
  for j in test:
    if j == '(':
      stack.append(i)
    elif j == ')':
      if stack:
        stack.pop()
      else:
        print("NO")
        break
  else:
    if not stack:
      print("YES")
    else:
      print("NO")

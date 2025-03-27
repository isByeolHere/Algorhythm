import sys
input = sys.stdin.readline

stack = []

n = input().strip()
bomb = input().strip()

stack = []

for char in n:
  stack.append(char)
  if len(stack) >= len(bomb):
    if ''.join(stack[-len(bomb):]) == bomb:
      for _ in range(len(bomb)):
        stack.pop()

if stack:
  print(''.join(stack))
else:
  print("FRULA")
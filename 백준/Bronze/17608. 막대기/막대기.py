import sys

n = int(sys.stdin.readline())

sticks = list(map(int, sys.stdin.read().split()))
stack = []

for i in range(n):
  if i == 0:
    stack.append(sticks[-1])
  elif sticks[-1-i] > stack[-1]:
    stack.append(sticks[-1-i])

print(len(stack))
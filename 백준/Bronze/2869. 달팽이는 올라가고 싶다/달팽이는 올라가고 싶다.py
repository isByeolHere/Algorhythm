import sys

A, B, V = map(int, sys.stdin.readline().split())

X = (V-B)/(A-B)

if X == int(X):
  print(int(X))
else:
  print(int(X)+1)
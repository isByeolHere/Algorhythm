import sys

a, b, c = (map(int, sys.stdin.read().split()))

multiply = a * b * c
multiply_str = str(multiply)

for i in range(10):
  count = multiply_str.count(str(i))
  print(count)
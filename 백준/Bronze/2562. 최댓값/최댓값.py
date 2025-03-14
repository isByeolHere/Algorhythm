import sys

num = [] 
for i in range(9): 
  a = int(sys.stdin.readline().strip())
  num.append(a)

max_value = max(num)
print(max_value)
print(num.index(max_value) + 1)
import sys

num = [] 
for i in range(9): 
  a = int(sys.stdin.readline().strip())
  num.append(a)

print(max(num))
print(num.index(max(num)) + 1)
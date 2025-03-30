import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
edges = []
for _ in range(e):
  edges.append(list(map(int,input().split())))
edges.sort(key=lambda x:x[2])

# Union-Find
parent = [i for i in range(v+1)]

def get_parent(x):
  if parent[x] == x:
    return x
  parent[x] = get_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  a = get_parent(a)
  b = get_parent(b)
  if a < b :
    parent[b] = a
  else:
    parent[a] = b

def same_parent(a, b):
  return get_parent(a) == get_parent(b)

ans = 0
for a, b, cost in edges:
  if not same_parent(a,b):
    union_parent(a, b)
    ans += cost

print(ans)
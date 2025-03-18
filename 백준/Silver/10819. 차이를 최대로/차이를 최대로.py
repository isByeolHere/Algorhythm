import sys


def permutate(arr, n):
  arr = sorted(nums)
  used = [False] * n
  max_sum = 0

  def generate(chosen, used):
    nonlocal max_sum
    if len(chosen) == n:
      dif_sum = 0 
      for j in range(1, n):
        dif_sum += abs(chosen[j-1]-chosen[j])
      max_sum = max(max_sum,dif_sum)
      return
    
    for i in range(len(arr)):
      if not used[i]:
        chosen.append(arr[i])
        used[i] = True
        generate(chosen, used)
        used[i] = False
        chosen.pop()

  generate([], used)
  return max_sum


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


result = permutate(nums, n)
print(result)
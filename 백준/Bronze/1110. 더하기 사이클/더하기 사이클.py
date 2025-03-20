# 더하기 사이클

import sys

def get_cnt(n, first, second, cnt):

    new_num = int(get_right(first)+get_right(second))
    cnt += 1
    if n == new_num:
      print(cnt)
      return
    get_cnt(n, new_num, get_sum(new_num), cnt)


def get_right(n):
    num_to_str = str(n)
    right = num_to_str[-1]
    return right

def get_sum(n):
  num_str = str(n) if n >= 10 else "0" + str(n)
  second = int(num_str[0])+int(num_str[1])
  return second

n = int(sys.stdin.readline())

get_cnt(n, n, get_sum(n),0)

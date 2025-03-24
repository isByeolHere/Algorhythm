import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
h = []
hq.heapify(h)

for _ in range(n):
    m = int(input())
    if m != 0:
        hq.heappush(h,-m)
    else:
        if h:
            print(-1 * int(hq.heappop(h)))
        else:
            print(0)
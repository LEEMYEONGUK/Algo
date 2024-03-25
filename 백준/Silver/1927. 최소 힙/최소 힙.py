from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    a = int(input())

    if a == 0:
        if hq:
            p = heappop(hq)
            print(p)
        else:
            print(0)

    else:
        heappush(hq, a)
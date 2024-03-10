# 마인크래프트
import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# min_v = 257
# max_v = 0
#
# for r in range(N):
#     for c in range(M):
#         if min_v > arr[r][c]:
#             min_v = arr[r][c]
#         if max_v < arr[r][c]:
#             max_v = arr[r][c]
result = [10**8, 0]

for h in range(257):
    work1 = 0
    work2 = 0
    for r in range(N):
        for c in range(M):
            num = h - arr[r][c]
            if num > 0:
                work2 += num
            if num < 0:
                work1 += abs(num)

    if B - work2 + work1 >= 0:
        time = work1 * 2 + work2 * 1
        if result[0] > time:
            result[0] = time
            result[1] = h
        if result[0] == time:
            if result[1] < h:
                result[1] = h

print(*result)

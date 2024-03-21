# 재귀함수 사용시 시간 초과
# import sys
# sys.setrecursionlimit(10**6)
# def recur(n):
#     if n < 4:
#         return 1
#     else:
#         return recur(n-3) + recur(n-2)

T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    # print(recur(N))

    # 메모이제이션 활용
    memo = [0] * (101)

    memo[1] = 1
    memo[2] = 1
    memo[3] = 1

    for i in range(4, N + 1):
        memo[i] = memo[i - 3] + memo[i - 2]

    print(memo[N])

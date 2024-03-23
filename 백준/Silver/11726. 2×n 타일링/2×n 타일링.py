# # 재귀 풀이
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# def find(n):
#     global cnt
#     if n > N:
#         return
#
#     if n == N:
#         cnt += 1
#         return
#     # for i in [n + 1, n + 2]:
#     find(n + 1)
#     find(n + 2)
#
# N = int(input())
# cnt = 0
#
# find(0)
# print(cnt % 10007)

# DP 풀이
N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N] % 10007)



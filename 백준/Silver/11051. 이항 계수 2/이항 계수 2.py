# 이항 계수 2
n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]
i = 1
j = 1
for i in range(1, n + 1):
    for j in range(0, i + 1):
        if j == 1:
            dp[i][j] = i
        if i == j or j == 0:
            dp[i][j] = 1
        if i >= 3 and i > j >= 2:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k] % 10007)
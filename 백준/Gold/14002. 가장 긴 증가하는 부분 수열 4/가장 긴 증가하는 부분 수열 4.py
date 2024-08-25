N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

result = []
max_index = max(dp)
print(max_index)

for i in range(N - 1, -1, -1):
    if dp[i] == max_index:
        result.append(lst[i])
        max_index -= 1

result.reverse()

print(*result)
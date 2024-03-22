# 구간 합 구하기4

N, M = map(int, input().split())
lst = list(map(int, input().split()))
n_sum = [0] * 100001

n = 0
for i in range(1, N + 1):
    n += lst[i - 1]
    n_sum[i] = n

for _ in range(M):
    a, b = map(int, input().split())
    print(n_sum[b] - n_sum[a-1])

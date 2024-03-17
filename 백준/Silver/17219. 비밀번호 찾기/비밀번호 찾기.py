N, M = map(int, input().split())

memo = dict()
for _ in range(N):
    a, b = map(str, input().split())
    memo[a] = b

for _ in range(M):
    print(memo[input()])
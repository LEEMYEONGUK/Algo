# N과 M (7)
def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return
    for j in range(N):
        dfs(n + 1, tlst + [lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# visited = [0] * (N + 1)
dfs(0, [])
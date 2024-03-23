def dfs(n, path):
    if n == M:
        print(*path)
        return
    for j in range(N):
        if lst[j] not in path:
            dfs(n + 1, path + [lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, [])
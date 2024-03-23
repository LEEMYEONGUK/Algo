def dfs(n, s, lst):
    if n == M:
        print(*lst)
        return
    for j in range(s, N + 1):
        dfs(n + 1, j, lst + [j])


N, M = map(int, input().split())
answer = []
dfs(0, 1, [])
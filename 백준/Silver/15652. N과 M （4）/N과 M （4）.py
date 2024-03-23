def dfs(n, s, lst):
    if n == M:
        for i in range(M-1):
            if lst[i] > lst[i + 1]:
                return
        print(*lst)
        return
    for j in range(s, N + 1):
        dfs(n + 1, j, lst + [j])


N, M = map(int, input().split())
answer = []
dfs(0, 1, [])
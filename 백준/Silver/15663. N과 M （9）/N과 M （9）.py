def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return
    prev = 0
    for j in range(N):
        if visited[j] == 0 and prev != lst[j]:
            prev = lst[j]
            visited[j] = 1
            dfs(n + 1, tlst + [lst[j]])
            visited[j] = 0

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [0] * N

dfs(0, [])
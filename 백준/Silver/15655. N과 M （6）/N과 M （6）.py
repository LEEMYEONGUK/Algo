# N과 M(6)

def dfs(n, s, tlst):
    if n == M:
        print(*tlst)
        return
    for j in range(s, N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, j + 1, tlst + [lst[j]])
            visited[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * (N + 1)
dfs(0, 0,[])

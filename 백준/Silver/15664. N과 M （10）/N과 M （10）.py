def dfs(n, s, tlst):
    if n == M:
        print(*tlst)
        return
    prev = 0
    for j in range(s, N):
        if visited[j] == 0 and prev != lst[j]:
            prev = lst[j]
            # 고른 인덱스 번호 안고를 수 있도록
            visited[j] = 1
            dfs(n + 1, j, tlst+[lst[j]])
            visited[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * (N + 1)
dfs(0, 0, [])
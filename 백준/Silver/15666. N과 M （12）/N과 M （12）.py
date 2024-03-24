# N과 M (12)

def dfs(n, s, tlst):
    if n == M:
        print(*tlst)
        return
    prev = 0
    for j in range(s, N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n + 1, j, tlst + [lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, 0, [])

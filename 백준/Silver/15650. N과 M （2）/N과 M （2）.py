# N 과 M (2)
def dfs(idx, path, used):
    if idx == N:
        if len(path) == M:
            path.sort()
            print(*path)
        return
    dfs(idx + 1, path + [lst[idx]], used + [lst[idx]])
    dfs(idx + 1, path, used)

N, M = map(int, input().split())
lst = list(range(1, N + 1))
dfs(0, [], [])
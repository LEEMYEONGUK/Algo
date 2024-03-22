# N과 M(1)
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(idx, path, used):
    if len(path) == M:
        print(*path)
        return
    for i in range(1, N + 1):
        if i not in used:
            dfs(idx + 1, path + [i], used + [i])

N, M = map(int, input().split())
dfs(0, [], [])

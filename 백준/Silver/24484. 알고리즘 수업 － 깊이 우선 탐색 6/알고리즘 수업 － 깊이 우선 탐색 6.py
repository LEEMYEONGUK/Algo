# 알고리즘 수업 - 깊이 우선 탐색6
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, j):
    global i
    visited[r] = i
    depth[r] = j
    for w in adjl[r]:
        if not visited[w]:
            i += 1
            dfs(w, j + 1)

N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
depth = [-1] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for l in adjl:
    l.sort(reverse=True)

i = 1
dfs(R, 0)

result = 0
for k in range(1, N + 1):
    result += depth[k] * visited[k]
print(result)
# 알고리즘 수업 - 깊이 우선 탐색 5
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, j):
    global i
    visited[r] = i
    depth[r] = j
    for k in adjl[r]:
        if not visited[k]:
            i += 1
            dfs(k, j + 1)


N, M, R = map(int, input().split())

# 정점의 깊이
depth = [-1] * (N + 1)
# 방문 순서
visited = [0] * (N + 1)

adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

# 오름차순 정렬
for l in adjl:
    l.sort()

i = 1
dfs(R, 0)

result = 0
for v in range(1, len(visited)):
    result += depth[v] * visited[v]
print(result)

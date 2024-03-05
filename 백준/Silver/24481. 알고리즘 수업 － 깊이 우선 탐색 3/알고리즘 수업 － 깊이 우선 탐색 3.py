import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, visited, i):
    visited[r] = i
    for j in adjl[r]:
        if visited[j] == -1:
            dfs(j, visited, i + 1)

N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for k in adjl:
    k.sort()

dfs(R, visited, 0)

for i in range(1, len(visited)):
    print(visited[i])

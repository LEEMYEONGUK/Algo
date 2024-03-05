#알고리즘 수업 - 깊이 우선 탐색4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, i):
    visited[r] = i
    for j in adjl[r]:
        if visited[j] == -1:
            dfs(j, i + 1)

N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for l in adjl:
    l.sort(reverse=True)

dfs(R, 0)

for v in range(1, len(visited)):
    print(visited[v])
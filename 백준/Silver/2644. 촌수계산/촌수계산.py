#촌수 계산
# 이동한 거리 구하는 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v, j):
    visited[v] = j
    for i in adjl[v]:
        if not visited[i]:
            dfs(i, j + 1)
N = int(input())

s, e = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    adjl[a].append(b)
    adjl[b].append(a)

dfs(s, 0)

if visited[e] == 0:
    print(-1)
else:
    print(visited[e])
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(r):
    global i
    visited[r] = i
    for j in adjl[r]:
        if not visited[j]:
            i += 1
            dfs(j)

N, M, R = map(int, input().split())
adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
for k in adjl:
    k.sort(reverse=True)

visited = [0] * (N + 1)
i = 1
dfs(R)

for v in range(1, len(visited)):
    print(visited[v])

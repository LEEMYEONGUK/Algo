#연결 요소의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(r):
    visited[r] = 1
    for i in adjl[r]:
        if not visited[i]:
            dfs(i)

N, M = map(int,input().split())
adjl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for k in adjl:
    k.sort()

cnt = 0
for j in range(1, N + 1):
    if visited[j] == 0:
        cnt += 1
        dfs(j)
print(cnt)

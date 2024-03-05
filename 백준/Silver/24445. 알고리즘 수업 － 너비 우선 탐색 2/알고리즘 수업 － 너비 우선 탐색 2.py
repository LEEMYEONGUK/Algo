from collections import deque
import sys
input = sys.stdin.readline


def bfs(r, j):
    visited[r] = j
    q = deque()
    q.append(r)

    while q:
        w = q.popleft()
        for i in adjl[w]:
            if not visited[i]:
                j += 1
                q.append(i)
                visited[i] = j


N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for k in adjl:
    k.sort(reverse=True)

visited = [0] * (N + 1)

bfs(R, 1)

for l in range(1, len(visited)):
    print(visited[l])

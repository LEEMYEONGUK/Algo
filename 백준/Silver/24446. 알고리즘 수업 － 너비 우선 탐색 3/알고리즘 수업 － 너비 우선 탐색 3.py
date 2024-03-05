from collections import deque

def bfs(r,visited):
    visited[r] = 0
    q = deque()
    q.append(r)
    while q:
        v = q.popleft()
        for w in adjl[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1

N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
visited =[-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

bfs(R, visited)

for i in range(1, len(visited)):
    print(visited[i])
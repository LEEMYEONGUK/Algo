from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        w = q.popleft()
        for j in adjl[w]:
            if not visited[j]:
                q.append(j)
                visited[j] = visited[w] + 1


N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
# print(adjl)
min_v = 1000000000
min_index = N + 1
for i in range(1, N+1):
    visited = [0] * (N + 1)
    bfs(i)
    # print(i, sum(visited))
    if min_v > sum(visited):
        min_v = sum(visited)
        min_index = i
    elif min_v == sum(visited):
        min_index = min(min_index, i)
print(min_index)


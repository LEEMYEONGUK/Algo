from collections import deque
import sys

input = sys.stdin.readline

def bfs(r, n):
    visited[r] = 0
    order[r] = n
    q = deque()
    q.append(r)

    while q:
        w = q.popleft()
        for j in adjl[w]:
            if visited[j] == -1:
                visited[j] = visited[w] + 1
                q.append(j)
                n += 1
                order[j] = n

N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
# 정점의 깊이
visited =[-1] * (N + 1)
# 방문 순서
order = deque([0] * (N + 1))


for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for k in adjl:
    k.sort()

bfs(R, 1)
result = 0
for i in range(1, len(visited)):
    if not visited[i] == -1:
        result += order[i] * visited[i]

print(result)
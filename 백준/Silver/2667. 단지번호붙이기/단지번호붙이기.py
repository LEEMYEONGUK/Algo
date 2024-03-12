# 단지 번호 붙이기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(sr, sc):
    cnt = 0
    visited[sr][sc] = 1
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        cnt += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return cnt

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

lst = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            lst.append(bfs(r, c))
print(len(lst))
lst.sort()
for i in range(len(lst)):
    print(lst[i])

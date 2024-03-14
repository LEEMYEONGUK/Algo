# 토마토
# BFS
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and adjm[nr][nc] == 0:
                que.append((nr, nc))
                adjm[nr][nc] = adjm[r][c] + 1

def find():
    max_v = -1
    for r in range(N):
        for c in range(M):
            if adjm[r][c] == 0:
                return -1
            if max_v < adjm[r][c]:
                max_v = adjm[r][c]
    return max_v - 1

M, N = map(int, input().split())
adjm = [list(map(int, input().split())) for _ in range(N)]

que = deque()
for r in range(N):
    for c in range(M):
        if adjm[r][c] == 1:
            que.append((r,c))

bfs()
print(find())

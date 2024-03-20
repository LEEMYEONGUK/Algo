# 빙산
import sys
# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from collections import deque

# 빙산을 녹이는 함수
def melt(sr, sc):
    m_visited[sr][sc] = 1
    m_cnt = 0
    for d in range(4):
        r = sr + dr[d]
        c = sc + dc[d]
        if 0 <= r < N and 0 <= c < M and arr[r][c] == 0 and m_visited[r][c] == 0:
            m_cnt += 1
    if arr[sr][sc] - m_cnt > 0:
        arr[sr][sc] -= m_cnt
    else:
        arr[sr][sc] = 0

# 빙산의 개수 확인하는 dfs
# def dfs(sr, sc):
#     visited[sr][sc] = 1
#     for d in range(4):
#         r = sr + dr[d]
#         c = sc + dc[d]
#         if 0 <= r < N and 0 <= c < M and arr[r][c] != 0 and visited[r][c] == 0:
#             dfs(r, c)

def bfs(sr, sc):
    visited[sr][sc] = 1
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(1, 100000):
    m_visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c]:
                melt(r, c)

    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] and visited[r][c] == 0:
                bfs(r, c)
                cnt += 1
    if cnt > 1:
        print(i)
        break
    if cnt == 0:
        print(0)
        break
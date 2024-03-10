# 유기농 배추
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

# visited 를 이용한 정석 풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if adjm[nr][nc] and not visited[nr][nc]:
            dfs(nr, nc)

T = int(input())
for _ in range(1, T + 1):
    M, N, K = map(int, input().split())
    # 배열을 넉넉하게 만들면 배열의 범위를 신경쓰지 않아도 됨
    adjm = [[0] * MAX for _ in range(MAX)]
    visited = [[0] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        adjm[y + 1][x + 1] = 1

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if adjm[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)
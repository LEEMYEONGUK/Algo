def find(r, c):
    global n

    visited[r][c] = 1
    cycle.append((r, c))

    if lst[r][c] == "U":
        nr, nc = r - 1, c
    elif lst[r][c] == "D":
        nr, nc = r + 1, c
    elif lst[r][c] == "L":
        nr, nc = r, c - 1
    elif lst[r][c] == "R":
        nr, nc = r, c + 1
    if 0 <= nr < N and 0 <= nc < M:
        # 방문한 곳이고 싸이클에 (nr, nc)가 포함되어 있따면
        if visited[nr][nc] == 1:
            if (nr, nc) in cycle:
                # 세이프 존 추가
                n += 1
        # 방문하지 않았으면 다음 위치로
        else:
            find(nr, nc)


N, M = map(int, input().split())

lst = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# print(lst)

# safe zone 의 개수
n = 0
for sr in range(N):
    for sc in range(M):
        if visited[sr][sc] == 0:
            cycle = []
            find(sr, sc)
# print(visited)

print(n)
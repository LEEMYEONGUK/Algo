from collections import deque

# visited[r][c][0] 에는 벽을 부수지 않은 상태의 visited 값을 저장
# visited[r][c][1] 에는 벽을 부순 상태의 visited 값을 저장
def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        r, c, wall = q.popleft()

        if r == N-1 and c == M - 1:
            return visited[r][c][wall]

        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 일반적인 bfs
                if lst[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                # 벽을 부실 수 있으면 부수고 진행! 이때 wall에 1을 넣어서 움직이니까 또 부수지 않음!
                if wall == 0 and lst[nr][nc] == 1:
                    q.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][wall] + 1
    return -1


N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0, 0)])

print(bfs())
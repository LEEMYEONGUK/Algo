from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    # 방문한 경로 저장할 큐 저장
    que = deque()
    que.append((r, c))
    # 방문 기록
    visited[r][c] = 1
    # 큐에 값이 있을 때까지 반복
    while que:
        r, c = que.popleft()
        # 목표 지점에 도착하였을 때 반복 종료
        if (r, c) == (N-1, M-1):
            break
        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 배열의 범위 벗어나지 않는지, 다음 경로가 이동할 수 있는 칸이고 방문하지 않은 곳인지 확인
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and visited[nr][nc] == 0:
                que.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

# 배열의 행과 열 입력 받기
N, M = map(int, input().split())
# 배열 정보 입력 받기
arr = [list(map(int, input())) for _ in range(N)]

# 방문 배열 만들기
visited = [[0] * M for _ in range(N)]

bfs(0, 0)
print(visited[N-1][M-1])

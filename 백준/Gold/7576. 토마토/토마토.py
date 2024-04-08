# 토마토
from collections import deque
def bfs():
    while q:
        r, c = q.popleft()
        # 상, 하, 좌, 우
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            # 안익은 토마토라면 큐 삽입
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and lst[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

def find():
    max_v = -1
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                print(-1)
                return
            max_v = max(max_v, visited[i][j])
    else:
        print(max_v - 1)
        return

# 입력값 받기
M, N= map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 큐 생성
q = deque()
# 방문 표시
visited = [[0] * M for _ in range(N)]
# 초기 토마토 상태 확인
flag = 0
# lst 값이 1 이면 큐에 넣고 bfs
# lst 값이 0 이 있으면 flag 1 저장 후 bfs, find 실행
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
        if lst[i][j] == -1:
            visited[i][j] = -1
        if lst[i][j] == 0:
            flag = 1

if flag:
    bfs()
    find()
# flag가 0이라는 것은 초기 토마토 상태에 0이 없다는 것
# 즉, 다 익은 상태
else:
    print(0)

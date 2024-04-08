from collections import deque

def bfs():
    # 큐에 값이 있는 동안 반복
    while q:
        h, r, c = q.popleft()
        # 층, 행, 열 변화
        for dh, dr, dc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]:
            nh, nr, nc = h + dh, r + dr, c + dc
            # 익은 토마토에 인접한 익지 않은 토마토 일때 방문
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and lst[nh][nr][nc] == 0:
                lst[nh][nr][nc] = lst[h][r][c] + 1
                q.append((nh, nr, nc))

def find():
    max_v = 1
    # 배열 순회하며 안 익은 토마토 있는 지 확인
    for i in range(N):
        for j in range(M):
            for k in range(H):
                max_v = max(max_v, lst[k][i][j])
                # 0인 값이 익지 않은 토마토이니까 -1 출력하고 반환
                if lst[k][i][j] == 0:
                    print(-1)
                    return
    # 반복문이 끝났을 때 최댓값이 1이라면 처음부터 다 익은 상태
    if max_v == 1:
        print(0)
        return
    # 하루가 지나 익은 토마토의 값이 2이니까 최댓값에서 1 빼서 출력
    else:
        print(max_v - 1)
        return


# 삼차원 배열(층)입력 받기
M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
# 삼차원 배열 순회하며 익은 토마토의 좌표 큐에 넣기
for i in range(N):
    for j in range(M):
        for k in range(H):
            if lst[k][i][j] == 1:
                q.append((k, i, j))

# 함수 실행
bfs()
find()

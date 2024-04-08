from collections import deque
N, L, R = map(int, input().split())

def bfs(sr, sc):
    # 종료 조건 확인용 변수 전역 변수 설정
    global flag
    # 큐 생성
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1
    # 지나온 지점들의 값의 합
    sm = lst[sr][sc]
    # 지나온 지점들의 좌표
    tlst=[(sr, sc)]
    # 지나온 거리
    cnt = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and L <= abs(lst[nr][nc] - lst[r][c]) <= R:
                visited[nr][nc] = 1
                q.append((nr, nc))
                tlst.append((nr, nc))
                sm += lst[nr][nc]
                cnt += 1
    # 시작 지점에서 이동하지 못했다면 다음 지점 탐색
    if cnt == 1:
        pass
    # 시작 지점에서 이동했다면 평균값으로 리스트 수정
    else:
        flag = 1
        for tr, tc in tlst:
            lst[tr][tc] = sm // cnt


lst = [list(map(int, input().split())) for _ in range(N)]

# 인구 이동 며칠 동안 걸리는지
answer = 0
# 연합을 만들 수 없을 때까지 반복
while True:
    # 방문 표시
    visited = [[0] * N for _ in range(N)]
    # 종료 조건 확인
    flag = 0
    # 모든 지점 탐색
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
    # 만약 플래그가 0이면 인구 이동 없었던 것 결과 출력
    if flag == 0:
        print(answer)
        break
    # 플래그 1 이면 인구 이동 하루 추가하기
    else:
        answer += 1

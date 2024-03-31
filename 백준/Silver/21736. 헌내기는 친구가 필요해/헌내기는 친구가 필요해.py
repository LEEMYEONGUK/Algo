# 헌내기는 친구가 필요해
from collections import deque

# 도연이의 위치 찾기
def find():
    for r in range(N):
        for c in range(M):
            if lst[r][c] == "I":
                return bfs(r, c)


def bfs(sr, sc):
    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    # 만난 사람 수
    cnt = 0
    q = deque()
    q. append((sr, sc))
    visited[sr][sc] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            # 그래프 탐색하며, 범위 내에 있는지, 방문 하지 않은 곳인지, 벽이 아닌지 확인
            if 0<= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and lst[nr][nc] != "X":
                q.append((nr, nc))
                visited[nr][nc] = 1
                # 사람 만났으면 cnt 1 증가
                if lst[nr][nc] == "P":
                    cnt += 1
    # 아무도 만나지 못했다면 TT 반환, 아니라면 cnt 반환
    if cnt == 0:
        return "TT"
    else:
        return cnt


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
print(find())
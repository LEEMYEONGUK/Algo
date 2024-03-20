# 안전 영역, DFS
import sys
sys.setrecursionlimit(10 ** 6)


# dfs 함수
def dfs(sr, sc, h):
    # 방문 체크
    visited[sr][sc] = 1
    # 4방향 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for d in range(4):
        r = sr + dr[d]
        c = sc + dc[d]
        # 이동한 정점이 배열을 벗어나지않고
        # 방문하지 않은 지점이고
        # 비의 양보다 높은 지점일때 탐색 진행
        if 0 <= r < N and 0 <= c < N and not visited[r][c] and h < arr[r][c]:
            dfs(r, c, h)

# 배열의 크기 및 높이 정보 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 구하기
max_h = 0
for r in range(N):
    for c in range(N):
        if max_h < arr[r][c]:
            max_h = arr[r][c]

# 안전 영역의 최대 갯수 저장 변수
max_cnt = 0

# 비의 양이 0 일때부터 모두 잠기는 양일때까지 반복
for h in range(max_h + 1):
    # 비의 양에 따라 방문 체크 배열과 안전영역의 개수 초기화
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    # 배열을 순회하며 탐색 진행
    for r in range(N):
        for c in range(N):
            # 방문하지 않은 지점이면서 비의 양보다 높을 때 탐색 시작하고
            # dfs 실행한 만큼 cnt 증가
            if visited[r][c] == 0 and h < arr[r][c]:
                dfs(r, c, h)
                cnt += 1
                
    # 탐색 종료 후 안전 영역의 최대 갯수 비교
    if max_cnt < cnt:
        max_cnt = cnt
        
# 결과(최대 안전 영역) 출력
print(max_cnt)
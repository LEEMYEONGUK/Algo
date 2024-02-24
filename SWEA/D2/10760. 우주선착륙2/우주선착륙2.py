# 착륙 지점으로 주변의 8개 구역의 사진을 찍기(착륙지점의 높이보다 낮은 구역만)
# 예비 후보지 지정(4개 이상의 사진을 찍을 수 있는 지점)
# 주변의 높이 정보가 없는 영역이 있어도 알려진 지역만(= 배열의 범위 넘어가면 안됨)
# 예비 후보지의 수를 출력

# 주변 방향, 8개 방위
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def solve():
    # 예비 후보지의 수
    cnt = 0
    # 사진의 수
    pic = 0
    
    # 배열의 모든 지점을 시작점으로 탐색
    for r in range(N):
        for c in range(M):
            # 8개 방향 탐색
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                # 시작점의 주변이 배열을 벗어나지 않고
                if 0 <= nr < N and 0 <= nc < M:
                    # 시작점의 높이보다 낮으면 pic(찍을 수 있는 사진의 수) 1 증가
                    if arr[r][c] > arr[nr][nc]:
                        pic += 1
                # 찍을 수 있는 사진이 4개 이상이면 cnt(예비 후보지의 수) 1 증가 후
                # 반복문 탈출(찍을 수 있는 사진의 정확한 수를 찾는게 아니기 때문에)
                if pic >= 4:
                    cnt += 1
                    break
            # 찍을 수 있는 사진의 수 초기화
            pic = 0
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    # N * M 배열 입력 받기
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 예비 후보지 수 출력
    print(f"#{test_case} {solve()}")

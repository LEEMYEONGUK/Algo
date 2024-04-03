#dr 북, 동, 남, 서
dj = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 왼쪽 회전 (현재 3)
# 2 -> 1 -> 0 -> 3
# (dr+3) % 4

# 북, 동, 남, 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solve(ci, cj, dr):
    # 청소한 공간 수
    cnt = 0
    # 청소기가 더 이상 움직이지 못할 때 종료
    while 1:
        # 현재 위치 청소
        arr[ci][cj] = 2
        cnt += 1

        # 왼쪽 방향으로 순서대로 탐색해서 미청소 영역이 있으면 이동
        flag = 1
        while flag == 1:
            # 왼쪽부터 네방향 중 미청소 영역 있는 경우
            for nd in ((dr+3) % 4, (dr+2) % 4, (dr+1) % 4, dr):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0: # 미청소 영역
                    ci, cj, dr = ni, nj, nd
                    flag = 0
                    break
            else:       # 4방향 모두 미청소 영역 없음 ===> 후진
                bi, bj = ci-di[dr], cj-dj[dr]       # 후진할 위치 계산
                if arr[bi][bj] == 1:        #벽이라면
                    return cnt
                else:
                    ci, cj = bi, bj


N, M = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve(si, sj, dr)
print(ans)

# 체스판 다시 칠하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 흰말부터 시작하는 체스판
W_chess = [["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"]]
# 검은말부터 시작하는 체스판
B_chess = [["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"]]

# 최솟값 비교를 위한 변수 저장
min_v = 65

# 배열 순회하며 시작 위치 바꾸기
# (8*8 배열과 비교하기 때문에 순회 끝나는 위치 주의)
for sr in range(N - 7):
    for sc in range(M - 7):
        w_cnt = 0
        b_cnt = 0
        # 배열의 일부분과 체스판 비교
        for r in range(8):
            for c in range(8):
                if arr[sr+r][sc+c] != W_chess[r][c]:
                    w_cnt += 1
                if arr[sr+r][sc+c] != B_chess[r][c]:
                    b_cnt += 1

        # 더 작은 값으로 최솟값 비교
        if w_cnt > b_cnt:
            if min_v > b_cnt:
                min_v = b_cnt
        else:
            if min_v > w_cnt:
                min_v = w_cnt
#결과 출력
print(min_v)


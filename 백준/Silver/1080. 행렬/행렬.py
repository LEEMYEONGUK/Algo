# 행렬

N, M = map(int, input().split())

# 입력 행렬
lst = [list(map(int, input())) for _ in range(N)]
# 목표 행렬
target_lst = [list(map(int, input())) for _ in range(N)]

# print(lst)
# print(target_lst)

# 3*3 행렬의 값 바뀐 횟수
cnt = 0
# 입력 행렬 순회
for r in range(N - 2):
    for c in range(M - 2):
        # 목표 행렬과 값이 다른 지점부터 3x3 만큼 값 바꾸기
        if lst[r][c] != target_lst[r][c]:
            for pr in range(r, r+3):
                for pc in range(c, c+3):
                    if lst[pr][pc] == 1:
                        lst[pr][pc] = 0
                    else:
                        lst[pr][pc] = 1
            # 값 바꿀 때 cnt 1증가
            cnt += 1

# 종료 시그널
end = 0

# 다 바꾼 다음 비교하기
for r in range(N):
    for c in range(M):
        # 다른 부분이 있으면
        if lst[r][c] != target_lst[r][c]:
            # -1 출력 하고 반복 탈출
            print(-1)
            # 이중 반복문 탈출하기 위한 플래그
            end = 1
            break
    # -1 출력 된 뒤 이중 반복문 탈출
    if end == 1:
        break
        
# 반복문이 끝까지 실행 되었다면 바뀐 횟수 출력
else:
    print(cnt)
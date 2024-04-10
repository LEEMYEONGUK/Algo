N = int(input())

# 빈자리 만들고 좋아하는 친구 리스트 입력 받기
seat = [[-1]*(N + 2)] +[[-1] + [0] * N + [-1] for _ in range(N)] +[[-1] * (N + 2)]
lst = [list(map(int, input().split())) for _ in range(N**2)]
s_lst = [[0]*(N + 2)] + sorted(lst)

# 좋아하는 친구 리스트를 순회하며 조건에 맞는 자리에 배치
for l in lst:
    empty_max = -1
    cnt_max = -1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 자리가 비어있지 않으면 다음 번호로
            if seat[i][j] > 0 : continue
            empty = cnt = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                # 인접한 빈칸의 수
                if seat[ni][nj] == 0:
                    empty += 1
                # 좋아하는 친구 수
                if seat[ni][nj] in l:
                    cnt += 1
            # 좋하하는 친구 수가 클때 or 좋아하는 친구 수가 같으면서 빈칸이 더 많을 때의 좌표 저장 
            if cnt_max < cnt or (cnt_max == cnt and empty_max < empty):
                cnt_max = cnt
                empty_max = empty
                ei, ej = i, j
    # 조건에 부합하는 자리에 배치
    seat[ei][ej] = l[0]

tbl = [0, 1, 10, 100, 1000]
result = 0
# 배치한 자리 순회하며 점수 계산
for r in range(1, N + 1):
    for c in range(1, N + 1):
        cnt = 0
        # 인접한 칸에 있는 좋아하는 친구수 계산
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if seat[nr][nc] in s_lst[seat[r][c]]:
               cnt += 1
        result += tbl[cnt]

print(result)

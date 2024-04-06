# 치킨 배달

# 남겨질 치킨집 좌표 구하기 및 치킨 거리 구하기
def dfs(n, r_lst):
    global result
    # 다 골랐으면

    if len(r_lst) > M:
        return

    if len(r_lst) == M:
        min_result = 0
        # 치킨집과 집의 거리 재기
        for x in range(len(h_lst)):
            min_v = 1000000
            for y in range(M):
                # 각각의 치킨집과 집의 거리중 가장 작은 값 찾기
                a = abs(r_lst[y][0] - h_lst[x][0]) + abs(r_lst[y][1] - h_lst[x][1])
                min_v = min(min_v, a)
            # 가장 작은 값 전체 값에 더해주기
            min_result += min_v
        result = min(min_result, result)

    if n == len(c_lst):
        return

    dfs(n + 1, r_lst+[c_lst[n]])
    dfs(n + 1, r_lst)

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 밎 집 좌표 찾기
c_lst = []
h_lst = []
for r in range(N):
    for c in range(N):
        if lst[r][c] == 2:
            c_lst.append((r, c))
        if lst[r][c] == 1:
            h_lst.append((r, c))

result = 1000000
dfs(0, [])
print(result)
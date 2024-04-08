def find(n, tlst):
    # tlst가 M보다 길어지면 리턴
    if len(tlst) > M:
        return 
    # 다 뽑았고, tlst의 길이가 M일때,
    if n == len(c_lst):
        if len(tlst) == M:
            result = 0
            # 집과 치킨집 각각의 거리 구하기
            for hr, hc in h_lst:
                min_v = 1000000
                # 치킨집 중에 가장 가까운 거리 result에 더하기
                for tr, tc in tlst:
                    min_v = min(min_v, (abs(hr-tr)+abs(hc-tc)))
                result += min_v
            # M개를 뽑은 치킨집의 치킨 거리 리스트에 삽입
            result_lst.append(result)
        return
    find(n + 1, tlst+[c_lst[n]])
    find(n + 1, tlst)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

h_lst = []
c_lst = []

# 치킨집, 집 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            h_lst.append((i, j))
        if arr[i][j] == 2:
            c_lst.append((i, j))

result_lst = []
find(0, [])
# 치킨 거리 리스트 중 최솟값 출력
print(min(result_lst))


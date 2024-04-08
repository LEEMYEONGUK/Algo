def find(n, tlst):
    if n == len(c_lst):
        if len(tlst) == M:
            result = 0
            for hr, hc in h_lst:
                min_v = 1000000
                for tr, tc in tlst:
                    min_v = min(min_v, (abs(hr-tr)+abs(hc-tc)))
                result += min_v
            result_lst.append(result)
        return
    find(n + 1, tlst+[c_lst[n]])
    find(n + 1, tlst)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

h_lst = []
c_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            h_lst.append((i, j))
        if arr[i][j] == 2:
            c_lst.append((i, j))

result_lst = []
find(0, [])
print(min(result_lst))


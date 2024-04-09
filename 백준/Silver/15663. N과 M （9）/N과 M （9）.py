# N과 M (9)
# 중복 제거

def dfs(n, tlst):
    if n == M:
        ans.append(tlst)
        return
    prev = 0
    for j in range(N):
        if v[j] == 0 and prev != lst[j]:
            prev = lst[j]
            v[j] = 1
            dfs(n + 1, tlst+[lst[j]])
            v[j] = 0
            # 다음 카드 고른 다음에 for j 로 올라가기 때문에 prev 초기 화 x

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
v = [0] * N
dfs(0, [])

for lst in ans:
    print(*lst)
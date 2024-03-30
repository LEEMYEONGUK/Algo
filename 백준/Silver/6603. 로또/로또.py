# 로또
def dfs(n, s, tlst):
    if n == 6:
        print(*tlst)
        return
    for j in range(s, k + 1):
        dfs(n + 1, j + 1, tlst+[lst[j]])


while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    else:
        k = lst[0]
        dfs(0, 1, [])
        print()
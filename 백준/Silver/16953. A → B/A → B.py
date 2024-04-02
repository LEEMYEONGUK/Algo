def dfs(n, s):
    global lst
    if s == B:
        lst.append(n)
        return
    if s > B:
        return
    dfs(n + 1, s * 2)
    dfs(n + 1, s * 10 + 1)

A, B = map(int, input().split())

lst = []
dfs(0, A)

if lst:
    print(min(lst) + 1)
else:
    print(-1)
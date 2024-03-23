def dfs(n, tlst):
    if n == M:
        answer.add(tuple(tlst))
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, tlst+[lst[j]])
            visited[j] = 0

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * 10001
answer = set()
dfs(0, [])

s_answer = sorted(answer)
for i in s_answer:
    print(*(list(i)))


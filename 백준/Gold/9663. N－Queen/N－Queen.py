def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    for j in range(N):
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n -j] = 1
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = 0

N = int(input())
# 방문 체크
v1 = [0] * N
# i행 j행의 합
# 오른쪽 대각선에 있으면 i, j 더한 값이 같음
v2 = [0] * N * 2
# i행 j행의 차
# 왼쪽 대각선에 있으면 i-j 를 뺀 값이 같음
# 파이썬은 -1 이면 뒤에서 찾으니까 절댓값으로 계산 안해도 괜찮
v3 = [0] * N * 2

ans = 0
dfs(0)
print(ans)
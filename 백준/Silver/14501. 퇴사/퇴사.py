# n 인덱스, v 비용
import sys
sys.setrecursionlimit(10**6)
def dfs(n, v):
    global answer
    if n >= N:
        if answer < v:
            answer = v
        return
    dfs(n+1, v)
    if n + T[n] <= N:
        dfs(n+T[n], v+P[n])

N = int(input())

T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

answer = 0
dfs(0, 0)
print(answer)

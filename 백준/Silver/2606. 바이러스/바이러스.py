import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r):
    visited[r] = 1
    for i in adjl[r]:
        if not visited[i]:
            dfs(i)


# 정점의 수
N = int(input())
# 간선의 수
M = int(input())

adjl = [[]for _ in range(N + 1)]
visited = [0] *(N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

dfs(1)
# 1번 컴퓨터가 걸린 바이러스 수 빼주기
print(sum(visited) - 1)

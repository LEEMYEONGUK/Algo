# 알고리즘 수업 - 깊이 우선 탐색1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
# r은 시작 정점, j는 출력 순서
def dfs(r):
    global j
    visited[r] = j
    for i in graph[r]:
        if not visited[i]:
            j += 1
            dfs(i)

# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, input().split())
# 그래프 정보 입력 받기
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# 오름차순 정렬
for g in graph:
    g.sort()

# 방문 표시
visited = [0] * (N + 1)

# 출력 순서
j = 1
# dfs 실행
dfs(R)

# 결과 출력
for k in range(1, N + 1):
    print(visited[k])
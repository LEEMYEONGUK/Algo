# 알고리즘 수업 - 너비 우선 탐색 1
from collections import deque

def bfs(r):
    # 전역 변수 설정
    global i
    # 방문 지점 표시
    visited = [0] * (N + 1)
    visited[r] = i
    # 큐 생성
    q = deque()
    q.append(r)
    while q:
        now = q.popleft()
        for next in adjl[now]:
            if visited[next] == 0:
                i += 1
                q.append(next)
                visited[next] = i

    return visited
N, M, R = map(int, input().split())

adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for k in adjl:
    k.sort()

# 방문 순서 저장을 위한 변수 저장
i = 1
v = bfs(R)
# 인덱스 0번 제외하고 출력
for j in range(len(v)):
    if j > 0:
        print(v[j])
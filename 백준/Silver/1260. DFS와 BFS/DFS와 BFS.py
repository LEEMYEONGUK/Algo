# DFS와 BFS

def dfs(v):
    d_visited[v] = 1
    print(v, end=" ")
    for i in adjl[v]:
        if not d_visited[i]:
            dfs(i)

def dfs2(v):
    stack = []
    stack.append(v)
    visited = [0] * (N + 1)
    visited[v] = 1
    print(v, end=" ")
    while True:
        for k in adjl[v]:
            if not visited[k]:
                stack.append(k)
                visited[k] = 1
                print(k, end=" ")
                v = k
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break


def bfs(v):

    que = []
    que.append(v)
    b_visited[v] = 1
    while que:
        now = que.pop(0)
        print(now, end=" ")
        for next in adjl[now]:
            if not b_visited[next]:
                que.append(next)
                b_visited[next] = 1

# N 정점의 개수, M 노드의 개수, V 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    adjl[a].append(b)
    adjl[b].append(a)

for i in adjl:
    i.sort()

d_visited = [0] * (N + 1)
b_visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
# 연산자 끼워넣기
def cal(t_lst):
    result = [0] * N
    result[0] = n_lst[0]
    for i in range(N-1):
        if t_lst[i] == "+":
            result[i+1] = result[i] + n_lst[i + 1]
        if t_lst[i] == "-":
            result[i+1] = result[i] - n_lst[i + 1]
        if t_lst[i] == "*":
            result[i+1] = result[i] * n_lst[i + 1]
        if t_lst[i] == "/":
            if result[i] < 0 and n_lst[i+1] > 0:
                result[i+1] = -(-result[i] // n_lst[i + 1])
            else:
                result[i+1] = result[i] // n_lst[i + 1]
    return result[N-1]

def dfs(n, tlst):
    global answer
    if n == N-1:
        # print(tlst)
        answer.append(cal(tlst))
        return
    for j in range(N - 1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, tlst + [lst[j]])
            visited[j] = 0


N = int(input())

n_lst = list(map(int, input().split()))
lst = []

a, b, c, d = map(int, input().split())
for _ in range(a):
    lst.append("+")
for _ in range(b):
    lst.append("-")
for _ in range(c):
    lst.append("*")
for _ in range(d):
    lst.append("/")

answer = []
visited = [0] * (N - 1)
dfs(0, [])

print(max(answer))
print(min(answer))
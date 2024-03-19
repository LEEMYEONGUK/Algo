N = int(input())

arr = [0] * 301
for i in range(1, N + 1):
    arr[i] = int(input())

visited = [0] * 301

visited[1] = arr[1]
visited[2] = arr[1] + arr[2]
visited[3] = max((arr[2] + arr[3]), (arr[1] + arr[3]))

for i in range(4, N + 1):
    visited[i] = max((visited[i-3] + arr[i-1] + arr[i]), visited[i-2] + arr[i])

print(visited[N])

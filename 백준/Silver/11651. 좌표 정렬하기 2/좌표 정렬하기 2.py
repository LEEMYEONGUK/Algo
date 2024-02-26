N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()
arr.sort(key=lambda x: x[1])
for i in range(N):
    a, b = arr[i]
    print(a, b)
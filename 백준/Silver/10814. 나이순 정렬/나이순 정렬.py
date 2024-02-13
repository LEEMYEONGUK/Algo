N = int(input())

lst = []

for _ in range(N):
    a, b = map(str, input().split())
    lst.append([int(a), b])

lst.sort(key=lambda x: x[0])

for i in lst:
    print(i[0], i[1])

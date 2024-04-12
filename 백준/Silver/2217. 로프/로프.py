# 로프

N = int(input())

lst = [0] * N

for i in range(N):
    lst[i] = int(input())
lst.sort(reverse=True)

max_v = lst[0]
for i in range(1, N):
    max_v = max(max_v, lst[i] * (i + 1))

print(max_v)
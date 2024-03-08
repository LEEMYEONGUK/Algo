import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
for _ in range(K):
    arr.append(int(input()))

s = 1
e = max(arr)

while s <= e:
    mid = (s + e)//2
    result = 0
    for i in arr:
        result += i // mid
    if result < N:
        e = mid - 1
    else:
        s = mid + 1
print(e)

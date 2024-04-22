# 게임을 만든 동준이

N = int(input())

lst = [int(input()) for _ in range(N)]
# print(lst)
cnt = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i - 1]:
        cnt += lst[i - 1] - lst[i] + 1
        lst[i - 1] = lst[i] - 1
print(cnt)
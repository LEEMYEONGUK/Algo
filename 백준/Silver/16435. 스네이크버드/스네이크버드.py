# 스네이크버드

N, L = map(int, input().split())

lst = sorted(list(map(int, input().split())))

for i in range(N):
    if L >= lst[i]:
        L += 1
    else:
        break
print(L)
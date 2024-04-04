# 시험 감독

N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())
# print(lst)
# sm = 0
# for i in range(N):
#     for j in range(100001):
#         if B * 1 + C * j >= lst[i]:
#             sm += (j + 1)
#             break
# print(sm)
# print(714290//5//7)

sm = 0
for i in range(N):
    if lst[i]-B >= 0:
        if (lst[i] - B) % C == 0:
            sm += (lst[i] - B) // C + 1
        else:
            sm += ((lst[i] - B) // C) + 2
    else:
        sm += 1
print(sm)
import sys
input = sys.stdin.readline

# N = (상근이가 가지고 있는 카드의 개수)
N = int(input())
# lst = (카드 리스트)
lst = sorted(list(map(int, input().split())))

# 확인하려는 수의 개수
M = int(input())

# 확인하는 수 리스트
num_list = list(map(int, input().split()))

# left = 0
# right = N - 1

# def binary (m, left, right):
#     if left > right:
#         return 0
#     mid = (left + right) // 2
#     if m == lst[mid]:
#         return cnt.get(m)
#     elif m < lst[mid]:
#         return binary(m, left, mid - 1)
#     elif m > lst[mid]:
#         return binary(m, mid + 1, right)

left = 0
right = N - 1

cnt = {}
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in num_list:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")

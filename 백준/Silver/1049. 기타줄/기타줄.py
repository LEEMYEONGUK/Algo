# 기타줄 적어도 N개 이상 사려고 함
# M개의 브랜드
N, M = map(int, input().split())

# a, b = 패키지 가격(6개), 낱개 가격

p_lst = [0] * M


lst = [0] * M

for i in range(M):
    a, b = map(int, input().split())
    p_lst[i] = a
    lst[i] = b

p_lst.sort()
lst.sort()

min_v = 0
if N % 6 == 0 and p_lst[0] < lst[0] * 6:
    min_v = p_lst[0] * (N//6)
else:
    if p_lst[0] >= lst[0] * 6:
        min_v = lst[0] * N
    else:
        min_v = min(p_lst[0] * (N//6 + 1), p_lst[0] * (N//6) + lst[0] * (N%6))

print(min_v)
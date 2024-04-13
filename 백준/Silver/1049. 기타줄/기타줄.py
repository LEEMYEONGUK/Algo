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
# and 뒤에 조건 추가 -> 패키지 가격이 낱개 6개 사는 거보다 비용이 적을때
if N % 6 == 0 and p_lst[0] < lst[0] * 6:
    min_v = p_lst[0] * (N//6)
else:
    # if 조건 추가 하니까 맞음 -> 낱개 6개 가격이 패키지 가격 보다 싸면 당연히 낱개로 구매
    if p_lst[0] >= lst[0] * 6:
        min_v = lst[0] * N
    else:
        # 패키지로 넉넉하게 사거나 낱개 추가해서 살 때 더 비용이 적은걸로 선택
        min_v = min(p_lst[0] * (N//6 + 1), p_lst[0] * (N//6) + lst[0] * (N%6))

print(min_v)
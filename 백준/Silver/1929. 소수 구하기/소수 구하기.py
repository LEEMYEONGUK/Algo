import sys
intput = sys.stdin.readline

# M, N 입력 받아 M ~ N 리스트 만들기
M, N = map(int, input().split())

# 숫자 리스트에서 하나씩 순회하며
for i in range(M, N + 1):
    if i == 1:
        continue
    # 1로만 나눠지는지 확인
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)

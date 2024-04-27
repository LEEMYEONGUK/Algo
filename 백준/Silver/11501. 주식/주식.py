# 주식

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    # 이익
    profit = 0

    # 주식의 최대 가격
    max_price = 0

    for i in range(N-1, -1, -1):
        if lst[i] > max_price:
            max_price = lst[i]
        # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
        else:
            profit += max_price - lst[i]

    print(profit)
T = int(input())

for test_case in range(1, T + 1):
    k = int(input())
    n = int(input())

    # k층 n호
    # k-1 층 1~n호 의 합
    # k-2 층 1, 1~2, 1~3 ...


    # 0층 1, 2, 3, 4, 5 ...

    zero_floor = [i for i in range(1, n+2)]
    # print(zero_floor)

    arr = [[0] * (n + 1) for _ in range(1, k + 2)]
    # print(arr)

    for r in range(k + 1):
        for c in range(n + 1):
            if r == 1:
                arr[r][c] = sum(zero_floor[:c + 1])
            else:
                arr[r][c] = sum(arr[r-1][:c + 1])

    for i in range(n + 1):
        arr[0][i] = zero_floor[i]

    # print(arr)

    print(arr[k][n - 1])



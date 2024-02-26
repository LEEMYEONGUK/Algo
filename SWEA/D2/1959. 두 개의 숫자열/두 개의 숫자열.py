T = int(input())

for test_case in range(1, T + 1):
    # A의 길의 N, B의 길이 M
    N, M = map(int, input().split())
    # A 숫자열, B 숫자열 입력 받기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 첫번째 케이스는 N < M 인 경우
    # 그러나 A가 클수도 B가 클수도 있기 때문에

    # A가 클 경우 N, M 및 A, B 바꿔주기
    if N > M:
        N, M = M, N
        A, B = B, A

    # 문제에서 주어진 조건으로 합의 최댓값 알 수 없으니 최대한 작은 값으로
    sum_max = -100000

    # A, N이 B, M보다 짧은 상황
    # A는 항상 0~N까지 반복
    # B는 한칸씩 옆으로 옮겨서 곱하고 더하기
    # B는 시작하는 지점이 M까지 아니라 N의 길이가 있기때문에 M - N까지만 시작점이 되면 됨
    # range함수에 넣어줄것이니 M - N에 1더하기
    for i in range(M - N + 1):
        sum_num = 0
        for j in range(N):
            # j는 0, 1, 2 ~ N-1 까지 i는 0, 1, 2 ~ (M - N)까지
            sum_num += B[j + i] * A[j]
        # 최댓값 비교후 재지정
        if sum_max < sum_num:
            sum_max = sum_num

    print(f"#{test_case} {sum_max}")
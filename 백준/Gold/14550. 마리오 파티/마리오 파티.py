# 마리오 파티

def find(N, S, T, lst):
    dp = [inf] * (N + 1)
    dp[0] = 0

    for _ in range(T - 1):
        temp_dp = [0] + [inf] * N
        for i in range(N + 1):
            if dp[i] != inf:
                for j in range(1, S + 1):
                    if i + j < N + 1:
                        temp_dp[i + j] = max(temp_dp[i + j], dp[i] + lst[i + j])
        dp = temp_dp
    max_v = max(dp[N + 1 - S:])
    return max_v


while True:
    try:
        N, S, T = map(int, input().split())
        lst = [0]
        if N == 0:
            break
        while len(lst) < N + 1:
            lst.extend(list(map(int, input().split())))
        # print(lst)
        inf = -1e9

        print(find(N, S, T, lst))

    except:
        break

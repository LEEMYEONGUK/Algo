T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    sm = sum(lst[0:M])
    start = 0
    end = M

    if N == M:
        if sm < K:
            cnt = 1
        else:
            cnt = 0
    else:
        cnt = 0
        while start < N:
            sm -= lst[start]
            sm += lst[end % N]
            if sm < K:
                cnt += 1
            start += 1
            end += 1
    print(cnt)
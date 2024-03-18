def fibo(N):
    if N > 1:
        for n in range(2, N + 1):
            lst1[n] = lst1[n-1] + lst1[n-2]
            lst0[n] = lst0[n-1] + lst0[n-2]

T = int(input())

for _ in range(T):
    N = int(input())
    lst0 = [0] * (N + 1)
    lst1 = [0] * (N + 1)
    lst0[0] = 1

    if N >= 1:
        lst1[1] = 1

    fibo(N)
    print(lst0[N], lst1[N])
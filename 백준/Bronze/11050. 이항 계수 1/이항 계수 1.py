N, K = map(int, input().split())

# nCr n! / (n-r)! * r!

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

print(int(fac(N) / (fac(N-K) * fac(K))))
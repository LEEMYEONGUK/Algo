# 보물

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

sm = 0
for i in range(N):
    sm += A[i] * B[i]

print(sm)
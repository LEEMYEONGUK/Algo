N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]

# 요세푸스 순열
yo = []

# 기존 순열 모두 제거 될 때까지
for _ in range(N):
    # 위치 좌로 3칸 이동 후
    for _ in range(K):
        arr.append(arr.pop(0))
    # 요세푸스 순열에 삽입
    yo.append(arr.pop())

print("<", end="")
print(*yo, sep=", ", end="")
print(">")
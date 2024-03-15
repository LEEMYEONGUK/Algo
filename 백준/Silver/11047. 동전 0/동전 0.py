import sys
input = sys.stdin.readline

# N은 동전의 개수, K는 목표 값
N, K = map(int, input().split())

# 목표 값 보다 작거나 같은 수만 lst에 입력 받기
lst = []
for _ in range(N):
    a = int(input())
    if a <= K:
        lst.append(a)
# 합계 및 동전의 수를 저장하기 위한 변수
sum = 0
cnt = 0

# 큰 값의 동전부터 더해보기
for j in range(len(lst) - 1, -1, -1):
    for i in range(K):
        cnt += 1
        sum += lst[j]
        # 목표값보다 커질경우 cnt 1 빼고, sum 해당하는 동전 빼주고 반복 탈출
        if sum > K:
            cnt -= 1
            sum -= lst[j]
            break
    # 다음으로 큰 동전 더하다가 목표값이랑 같아졌을 때 반복문 탈출
    if sum == K:
        break

print(cnt)

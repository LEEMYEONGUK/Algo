# 주유소
N = int(input())

# 거리 리스트
l_lst = list(map(int, input().split()))

# 주유 비용
c_lst = list(map(int, input().split()))
# 마지막 지점에 도착하면 주유 할 필요 없으니 마지막 값 빼기
c_lst.pop()

# 최소 주유 비용
min_v = 1000000001
# 주유 비용 합계
answer = 0
for i in range(N - 1):
    # 거쳐온 지점 중 최소 주유 비용에 이동 거리 곱해주기
    min_v = min(min_v, c_lst[i])
    answer += l_lst[i] * min_v

# 결과 출력
print(answer)
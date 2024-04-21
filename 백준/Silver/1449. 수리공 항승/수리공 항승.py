# 수리공 항승

N, L = map(int, input().split())

lst = list(map(int, input().split()))
# 물이 새는 곳 오름차순으로
lst.sort()

# d 물이 새는 곳 테이프로 막았을 때 같이 막히는 범위
# 좌우 0.5만큼 간격 주니까 -1 해주기
d = lst[0] + L - 1
# 테이프를 붙인 횟수
cnt = 1

# 배열을 순회하면서 테이프로 막은 범위를 넘어 섰을 때 다시 테이프 붙이기
for i in range(N):
    if lst[i] > d:
        d = lst[i] + L - 1
        cnt += 1
print(cnt)
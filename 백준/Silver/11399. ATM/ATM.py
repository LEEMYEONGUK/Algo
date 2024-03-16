import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
# 기다리는 시간이 최소가 되기 위해 오름차순으로 정렬
lst.sort()

# 줄을 서 있는 사람 전부가 기다리는 시간
total_time = 0
# 각 사람이 기다리는 시간
time = 0

# 앞에서 부터 기다리는 시간 더해주고
# 더한 결과를 전체 시간에 더해주기
for i in range(len(lst)):
    time += lst[i]
    total_time += time

print(total_time)

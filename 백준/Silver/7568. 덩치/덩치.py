# 몸무게와 키가 더 크면 덩치가 크다고 이야기함
# 덩치 등수는 자신보다 덩치가 큰 사람의 수 + 1등

# N명의 정보 리스트로 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각각 다른 사람들과 한번씩 비교해서 몸무게랑 키 모두 더 클경우 cnt 증가
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    # cnt에 1을 더하여 출력        
    print(cnt + 1, end=" ")
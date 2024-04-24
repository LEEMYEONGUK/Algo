# 신입사원

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        lst[i] = (a, b)
    # 왼쪽 등수 기준으로 정렬
    lst.sort()

    # 왼쪽 점수가 1등인 사람은 무조건 붙음
    cnt = 1
    max_v = lst[0][1]
    
    # lst 순회하면서 왼쪽 점수가 1등인 사람의 오른쪽 점수보다 작으면(등수가 높으면) 채용 가능! 
    # 그리고 비교하는 값을 채용된 사람의 오른쪽 점수로 설정
    # 정방향으로 순회하니까 무조건 왼쪽 등수는 낮음 그러니까 오른쪽 등수가 높아야함(숫자가 작아야함) 
    for i in range(1, N):
        if lst[i][1] < max_v:
            cnt += 1
            max_v = lst[i][1]
    print(cnt)
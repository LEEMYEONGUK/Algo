T = int(input())

for _ in range(1, T + 1):
    N = int(input())

    # 각 의상 종류에 따른 의상의 수 입력 받기
    dic = dict()
    for _ in range(N):
        a, b = map(str, input().split())
        # 키(의상 종류)가 없다면 키에 값 1을 할당
        if not dic.get(b):
            dic[b] = 1
        # 키가 딕셔너리에 존재한다면 값 1 증가
        else:
            dic[b] += 1
    
    # 딕셔너리의 값을 순회하며 곱해주기
    # 경우의 수 각 의상의 종류를 0개, 1개, ~ 고를 경우 = i + 1
    num = 1
    for i in dic.values():
        num *= (i + 1)
    
    # 전부 고르지 않을 경우 1 빼주기
    print(num - 1)
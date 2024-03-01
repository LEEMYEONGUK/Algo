# 난이도 30% 절사 평균
# 위에서 15%(반올림) 아래에서 15%(반올림) 평균 계산 반영x
# 의견이 없을 경우 0으로 결정


# 반올림 함수
def round(x):
    # x의 소수부분이 0.5와 1 사이라면 올림
    if 0.5 <= (x - int(x)) < 1:
        return int(x) + 1
    else:
        return int(x)


def solve():
    # 배열 정렬
    arr.sort()
    # 15% 계산
    del_num = N * 0.15
    # N * 0.15 값 반올림하기
    r_del_num = round(del_num)
    # 필요한 범위로만 슬라이싱하기
    n_arr = arr[r_del_num: N - r_del_num]
    # 평균 값 반환
    return round(sum(n_arr)/(N - r_del_num * 2))


N = int(input())
arr = []

# 의견이 없을 경우 0 출력
if N == 0:
    print(0)

else:
    for _ in range(N):
        arr.append(int(input()))
    print(solve())

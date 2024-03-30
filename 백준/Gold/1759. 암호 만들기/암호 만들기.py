# 암호 만들기
def dfs(n, s, answer):
    cnt = 0
    if n == L:
        for a in answer:
            if a in ["a", "e", "i", "o", "u"]:
                cnt += 1
        # cnt 모음의 개수, L - cnt : 자음의 개수
        if cnt > 0 and L - cnt >= 2:
            print(answer)
        return
    for j in range(s, C):
        dfs(n + 1, j + 1, answer + lst[j])

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
dfs(0, 0, "")


def dfs(sr, er, sc, ec):
    global white, blue

    color = lst[sr][sc]
    for r in range(sr, er):
        for c in range(sc, ec):
            if color != lst[r][c]:
                dfs(sr, (sr+er)//2, sc, (sc+ec)//2)
                dfs(sr, (sr+er)//2, (sc+ec)//2, ec)
                dfs((sr+er)//2, er, sc, (sc+ec)//2)
                dfs((sr+er)//2, er, (sc+ec)//2, ec)
                return
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return


N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

# print(lst)
white = 0
blue = 0
dfs(0, N, 0, N)
print(white)
print(blue)
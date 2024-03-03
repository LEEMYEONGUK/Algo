T = int(input())

def solve():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_v = 0
    for r in range(N):
        for c in range(M):
            sum = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    sum += arr[nr][nc]

            if max_v < sum:
                max_v = sum

    return max_v


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {solve()}")


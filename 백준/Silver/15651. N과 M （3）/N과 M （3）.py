# N 과 M (3)
# 기존 순열 알고리즘에서 used 빼기
# 중복을 허용하는 순열이기 때문에 중복 체크 불필요
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(level, path):
    if len(path) == M:
        print(*path)
        return
    for i in range(1, N + 1):
        dfs(level + 1, path+[i])

N, M = map(int, input().split())
dfs(0, [])

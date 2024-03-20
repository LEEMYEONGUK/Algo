import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def find(level):
    global cnt
    if sum(selected) == N:
        cnt += 1
    if level == N:
        return
    for i in range(1, 4):
        selected.append(i)
        find(level + 1)
        selected.pop()


for _ in range(1, T + 1):
    N = int(input())
    selected = []
    cnt = 0
    find(0)
    print(cnt)
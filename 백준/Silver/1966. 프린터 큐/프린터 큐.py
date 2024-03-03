from collections import deque

T = int(input())

def enque(x, y):
    global rear
    rear += 1
    que[rear] = (x, y)


def solve(z):
    while que:
        max_v = max(que)
        a = que.popleft()
        if a[0] == max_v[0]:
            print_order.append(a)
        else:
            que.append(a)


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    front = -1
    rear = -1

    que = deque([0] * N)
    arr = list(map(int, input().split()))

    y = 0
    for x in arr:
        enque(x, y)
        y += 1

    print_order = []
    solve(print_order)

    for x, y in print_order:
        if y == M:
            print(print_order.index((x, y)) + 1)
from collections import deque

que = deque([])

def push_front(x):
    que.appendleft(x)

def push_back(x):
    que.append(x)

def pop_front():
    if que:
        print(que.popleft())
    else:
        print(-1)

def pop_back():
    if que:
        print(que.pop())
    else:
        print(-1)

def size():
    print(len(que))

def empty():
    if que:
        print(0)
    else:
        print(1)

def front():
    if que:
        print(int(que[0]))
    else:
        print(-1)
def back():
    if que:
        print(que[-1])
    else:
        print(-1)

N = int(input())

arr = [list(input().split()) for _ in range(N)]

for i in range(len(arr)):
    if arr[i][0] == "push_front":
        push_front(int(arr[i][1]))
    elif arr[i][0] == "push_back":
        push_back(int(arr[i][1]))
    elif arr[i][0] == "pop_front":
        pop_front()
    elif arr[i][0] == "pop_back":
        pop_back()
    elif arr[i][0] == "size":
        size()
    elif arr[i][0] == "empty":
        empty()
    elif arr[i][0] == "front":
        front()
    elif arr[i][0] == "back":
        back()

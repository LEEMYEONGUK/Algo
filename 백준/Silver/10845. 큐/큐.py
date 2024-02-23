que = []

def push(x):
    que.append(x)

def pop():
    if que:
        print(que.pop(0))
    else:
        print(-1)

def size():
    print(len(que))

def empty():
    if not que:
        print(1)
    else:
        print(0)

def front():
    if que:
        print(que[0])
    else:
        print(-1)

def back():
    if que:
        print(que[-1])
    else:
        print(-1)

T = int(input())

arr = [list(input().split()) for _ in range(T)]
#print(arr)
for i in range(len(arr)):
    if arr[i][0] == "push":
        push(int(arr[i][1]))
    elif arr[i][0] == "pop":
        pop()
    elif arr[i][0] == "size":
        size()
    elif arr[i][0] == "empty":
        empty()
    elif arr[i][0] == "front":
        front()
    elif arr[i][0] == "back":
        back()

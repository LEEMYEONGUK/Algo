N = int(input())

def push(x):
    stack.append(x)

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)
def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

stack = []
lst = []
for _ in range(N):
    lst.append(list(map(str, input().split())))
for i in lst:
    if i[0] == "push":
        push(int(i[1]))
    elif i[0] == "pop":
        pop()
    elif i[0] == "size":
        size()
    elif i[0] == "empty":
        empty()
    elif i[0] == "top":
        top()

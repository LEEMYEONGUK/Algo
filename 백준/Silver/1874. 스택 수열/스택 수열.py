import sys
input = sys.stdin.readline

# 스택 수열
N = int(input())

stack = []
result = []
find = True

# push
now = 1

for _ in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        find = False
        break

if not find:
    print("NO")
else:
    for i in result:
        print(i)
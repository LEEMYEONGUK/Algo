# 펠린드롬 만들기

lst = list(input())

lst.sort()

stack = []
result = ""
for i in range(len(lst)):
    if stack and stack[-1] == lst[i]:
        result += stack.pop()
    else:
        stack.append(lst[i])
# print(stack)
# print(result)
a = len(result)
if len(stack) > 1:
    print('I\'m Sorry Hansoo')
else:
    if len(stack) % 2 == 0:
        for i in range(a-1, -1, -1):
            result += result[i]
        print(result)

    if len(stack) % 2 == 1:
        result += stack.pop()
        for i in range(a-1, -1, -1):
            result += result[i]
        print(result)

# 펠린드롬 만들기

# 입력 받기
lst = list(input())
lst.sort()

# 짝이 맞는 지 확인할 stack 만들기
stack = []
# 펠린드롬 수 만들기 위한 변수
result = ""

# lst 순회하며 stack에 append
# stack의 마지막 문자와 같다면 stack에 있는 거 pop 해주고 result에 더해주기
for i in range(len(lst)):
    if stack and stack[-1] == lst[i]:
        result += stack.pop()
    else:
        stack.append(lst[i])

# 반쪽 자리 펠린드롬 수 길이 저장
a = len(result)

# stack의 길이가 1보다 크다면 펠린드롬 수 만들지 못함!
if len(stack) > 1:
    print('I\'m Sorry Hansoo')
else:
    # stack에 남아있는 게 없는 경우
    # result의 뒤의 문자부터 result에 더해주기
    if len(stack) % 2 == 0:
        for i in range(a-1, -1, -1):
            result += result[i]
        print(result)
        
    # stack에 남아있는 게 하나인 경우
    # result에 더해주고
    # 더해준거 제외하고 뒤의 문자부터 result에 더해주기
    if len(stack) % 2 == 1:
        result += stack.pop()
        for i in range(a-1, -1, -1):
            result += result[i]
        print(result)

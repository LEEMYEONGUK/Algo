# 잃어버린 괄호

lst = list(input().split("-"))

# print(lst)
answer = 0
for i in lst[0].split("+"):
    answer += int(i)
for i in lst[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)
# 회의실 배정

N = int(input())

lst = [0] * N

for i in range(N):
    a, b = map(int, input().split())
    lst[i] = (a, b)

# print(lst)
lst.sort(key=lambda x: (x[1], x[0]))
# print(lst)

end_time = 0
cnt = 0
for l in lst:
    if end_time <= l[0]:
        cnt += 1
        end_time = l[1]

print(cnt)
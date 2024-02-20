from collections import deque

# 1부터 N까지 N개의 수
N = int(input())

arr = deque()
# print(arr)

for i in range(1, N + 1):
    arr.append(i)
# print(arr)

# 카드 버리기 및 맨 앞장 카드 뒤로 옮기기 반복
while (len(arr) > 1):
    arr.popleft()
    a = arr.popleft()
    arr.append(a)

print(arr[0])

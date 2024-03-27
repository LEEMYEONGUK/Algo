# 좌표압축
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
s_lst = sorted(set(lst))
dic = dict()
answer = [0] * N
for i in range(len(s_lst)):
    dic[s_lst[i]] = i
for i in range(N):
    answer[i] = dic[lst[i]]
print(*answer)
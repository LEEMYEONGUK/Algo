import sys
input = sys.stdin.readline
N, M = map(int, input().split())

p_dic = dict()
n_dic = dict()
for i in range(1, N + 1):
    p = input().strip()
    p_dic[p] = i
    n_dic[i] = p
    
# print(p_dic)
# print(n_dic)

for _ in range(M):
    a = input().strip()
    if a.isdigit():
        print(n_dic[int(a)])
    else:
        print(p_dic[a])
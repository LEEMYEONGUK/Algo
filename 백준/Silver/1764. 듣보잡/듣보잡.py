# 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

a_set = set()
b_set = set()

for _ in range(N):
    a_set.add(input().strip())

for _ in range(M):
    b_set.add(input().strip())

# a집합과 b집합의 교집합을 리스트로 형변환
lst = list(a_set.intersection(b_set))

lst.sort()
print(len(lst))
print(*lst, sep="\n")
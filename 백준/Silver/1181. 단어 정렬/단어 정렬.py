N = int(input())

lst = []

for _ in range(N):
    lst.append(input())

lst = set(lst)
lst = list(lst)

lst.sort()
lst.sort(key=len)

print(*lst, sep="\n")
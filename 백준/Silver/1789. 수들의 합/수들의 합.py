S = int(input())

sm = 0
for i in range(1, 10**6):
    sm += i
    if sm == S:
        print(i)
        break
    if sm > S:
        print(i-1)
        break
    
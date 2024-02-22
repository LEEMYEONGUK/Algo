N = int(input())

arr = [str(i) for i in range(1, N + 1)]

for i in arr:
    cnt = 0
    if "3" in i:
        cnt += i.count("3")
    if "6" in i:
        cnt += i.count("6")
    if "9" in i:
        cnt += i.count("9")
    if cnt == 0:
        arr[arr.index(i)] = i
    else:
        arr[arr.index(i)] = "-" * cnt

print(*arr)
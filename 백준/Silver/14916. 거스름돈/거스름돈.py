n = int(input())
cnt = 0

if n % 5 == 0:
    print(n//5)
else:
    while True:
        n -= 2
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            break
        if n < 0:
            cnt = -1
            break

    print(cnt)
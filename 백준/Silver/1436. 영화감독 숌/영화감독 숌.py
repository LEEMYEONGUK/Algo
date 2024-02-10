N = int(input())
s_list = []

for i in range(1, 10000001):
    cnt = 0
    for s in str(i) + "0":
        if s == "6":
            cnt += 1
        else:
            if cnt >= 3:
                s_list.append(i)
                break
            else:
                cnt = 0
print(s_list[N - 1])
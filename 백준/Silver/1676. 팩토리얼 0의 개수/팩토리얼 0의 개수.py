N = int(input())

def fac(n):
    if n < 1:
        return 1
    else:
        return n * fac(n - 1)

# print(fac(N))

fac_list = list(str(fac(N)))
fac_list.reverse()

# print(fac_list)

cnt = 0
for i in fac_list:
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)